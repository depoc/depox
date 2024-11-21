from django.utils.timezone import now, localtime
from datetime import timedelta
from django.db.models.functions import TruncDate

from .models import BankAccount, Transactions
from .forms import TransactionsForm, BankAccountForm


class Finance:
    @staticmethod
    def context(request) -> dict:
        context = {}
        context.update(Finance.add_transactions(request))
        context.update(Finance.get_transactions_by_date(request))
        context.update(Finance.add_bank_account(request))
        return context

    @staticmethod
    def add_transactions(request) -> dict:
        """
        Lida com a lógica de adicionar transações e calcula o saldo total das contas bancárias.
        """
        form = TransactionsForm(user=request.user)
        tipo = request.POST.get('tipo')

        if request.method == 'POST' and 'add-transaction' in request.POST:
            form = Finance._process_transaction(request, form, tipo)

        # Dados da empresa e bancos
        company = request.user.company
        banks = BankAccount.objects.filter(company=company)

        # Cálculo do saldo total
        saldo_total = sum(bank.saldo for bank in banks)

        return {'transaction': form, 'saldo_total': saldo_total, 'banks': banks}

    @staticmethod
    def _process_transaction(request, form, tipo) -> TransactionsForm:
        """
        Processa uma transação, atualiza o saldo do banco e salva o formulário de transação.
        """
        post_data = request.POST.copy()
        valor = post_data.get('valor', '')
        valor_cleaned = valor.replace('.', '').replace(',', '.')

        if valor:
            if tipo == 'receber':
                valor = float(valor_cleaned)
                post_data['valor'] = valor

            elif tipo == 'pagar':
                valor = float(valor_cleaned) * (-1)
                post_data['valor'] = valor

            elif tipo == 'transferir':
                valor = float(valor_cleaned) * (-1)

                origin_account = BankAccount.objects \
                    .get(id=post_data['conta'])
                destination_account = BankAccount.objects \
                    .get(id=post_data['conta2'])                   
                
                post_data['valor'] = valor      
                post_data['contato'] = request.user.name              
                post_data['descricao'] = f'enviada → {destination_account}'          

        post_data['created_by'] = request.user
        form = TransactionsForm(post_data, user=request.user)
        if form.is_valid() and valor != 0:
            transaction = form.save()
            if tipo == 'transferir':
                transfer_to_destination_account = Transactions(
                tipo = 'transferir',
                valor = valor * (-1),
                conta = destination_account,
                contato = request.user.name,
                descricao = f'recebida ← {origin_account}',
                categoria = 'transferência',
                created_by = request.user,
                linked=transaction,
                )                     
                transfer_to_destination_account.save()

        return form
    
    @staticmethod
    def get_transactions_by_date(request) -> dict:
        today = localtime(now()).date()
        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=6)
        start_of_month = today.replace(day=1)

        if today.month == 12:
            next_month = today.replace(year=today.year + 1, month=1, day=1)
        else:
            next_month = today.replace(month=today.month + 1, day=1)
            
        end_of_month = next_month - timedelta(days=1)        

        company = request.user.company
        banks = BankAccount.objects.filter(company=company)

        transactions = (
            Transactions.objects
            .filter(conta__in=banks)
            .annotate(date=TruncDate('created'))
            .order_by('-created')
        )                        

        conta = request.GET.get('banco')
        data = request.GET.get('data')

        if conta:
            transactions = transactions.filter(conta=conta)        

        if data == 'hoje':
            transactions = transactions.filter(created__date=today)
        elif data == 'semana':
            transactions = transactions.filter(
                created__date__gte=start_of_week,
                created__date__lte=end_of_week,
            )
        elif data == 'mes':
            transactions = transactions.filter(
                created__date__gte=start_of_month,
                created__date__lte=end_of_month,
            )    

        transactions_group = {}
        for transaction in transactions:
            date = transaction.date
            if date not in transactions_group:
                transactions_group[date] = []
            transactions_group[date].append(transaction)   

        context = {
            'transactions_group': transactions_group,
            'current_date': now,            
        }
        context.update(Finance._get_balance(transactions))

        return context                 

    @staticmethod
    def _get_balance(transactions) -> dict:
        recebimentos = 0
        for transaction in transactions:
            if transaction.tipo == 'receber':
                recebimentos += transaction.valor

        pagamentos = 0
        for transaction in transactions:
            if transaction.tipo == 'pagar':
                pagamentos += transaction.valor

        balanco = (recebimentos) - (-pagamentos)

        return {          
            'pagamentos': pagamentos,
            'recebimentos': recebimentos,
            'balanco': balanco,
        }                    
    
    @staticmethod
    def add_bank_account(request) -> dict:
        form = BankAccountForm()      

        post_data = request.POST.copy()
        saldo = post_data.get('saldo', '')
        post_data['company'] = request.user.company
        post_data['saldo'] = 0

        if request.method == 'POST' and 'add-account' in request.POST:
            form = BankAccountForm(post_data)
            if form.is_valid():
                bank_account = form.save()

            if saldo:
                saldo_cleaned = saldo.replace('.', '').replace(',', '.')     
                transaction = Transactions(
                        tipo='receber',
                        valor=saldo_cleaned,
                        conta=bank_account,
                        contato='...',
                        descricao='saldo inicial',
                        categoria='...',
                        created_by=request.user,
                    )     
                transaction.save()           

        context = {} 
        # atualiza o saldo total automaticamento ao criar nova conta
        banks = BankAccount.objects.filter(company=request.user.company)
        saldo_total = sum(bank.saldo for bank in banks)
        # atualiza o transações automaticamento ao criar nova conta
        context.update(Finance.get_transactions_by_date(request))   

        context.update({'bank_account_form': form, 'saldo_total': saldo_total})
        return context