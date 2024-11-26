from django.utils.timezone import now, localtime
from django.db.models.functions import TruncDate

from datetime import timedelta

from decimal import Decimal, InvalidOperation

from .models import BankAccount, Transactions
from .forms import TransactionsForm, BankAccountForm


class Finance:
    @staticmethod
    def context(request) -> dict[str, object]:
        context = {}
        context.update(Finance.add_transactions(request))
        context.update(Finance.get_transactions_by_date(request))
        context.update(Finance.add_bank_account(request))
        context.update(Finance.edit_bank_account(request))
        return context

    @staticmethod
    def add_transactions(request) -> dict[str, object]:
        form: TransactionsForm = TransactionsForm(user=request.user)
        tipo: str = request.POST.get('tipo')

        if request.method == 'POST' and 'add-transaction' in request.POST:
            form = Finance._process_transaction(request, form, tipo)

        company = request.user.company
        banks = BankAccount.objects.filter(company=company).order_by('-saldo')

        saldos: list = [bank.saldo for bank in banks]
        saldo_total: Decimal = Decimal(sum(saldos))

        return {'transaction': form, 'saldo_total': saldo_total, 'banks': banks}

    @staticmethod
    def _process_transaction(request, form, tipo) -> TransactionsForm:
        post_data = request.POST.copy()

        if valor := post_data.get('valor', ''):
            try:
                valor_cleaned = abs(Decimal(valor.replace('.', '').replace(',', '.')))
            except InvalidOperation:
                raise ValueError("invalid monetary value format")
            
            if tipo == 'receber':
                post_data['valor'] = valor_cleaned

            elif tipo == 'pagar':
                post_data['valor'] = -valor_cleaned

            elif tipo == 'transferir':
                post_data['valor'] = -valor_cleaned 

                origin_account = BankAccount.objects \
                    .get(id=post_data['conta'])
                destination_account = BankAccount.objects \
                    .get(id=post_data['conta2'])                   
                     
                post_data['contato'] = request.user.name              
                post_data['descricao'] = f'enviada → {destination_account}'          

        post_data['created_by'] = request.user
        form = TransactionsForm(post_data, user=request.user)
        if form.is_valid() and valor_cleaned != 0:
            transaction = form.save()
            if tipo == 'transferir':
                transfer_to_destination_account = Transactions(
                tipo = 'transferir',
                valor = valor_cleaned,
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
    def get_transactions_by_date(request) -> dict[str, object]:
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

        transactions_group: dict = {}
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
    def _get_balance(transactions) -> dict[str, object]:
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
    def add_bank_account(request) -> dict[str, object]:
        form = BankAccountForm()      
        post_data = request.POST.copy()
        saldo = post_data.get('saldo', '')

        if request.method == 'POST' and 'add-account' in request.POST:
            post_data['company'] = request.user.company
            post_data['saldo'] = 0
            form = BankAccountForm(post_data)

            if form.is_valid():
                bank_account = form.save()

                if saldo:
                    saldo_cleaned = saldo.replace('.', '').replace(',', '.')     
                    Transactions.objects.create(
                            tipo='receber',
                            valor=saldo_cleaned,
                            conta=bank_account,
                            contato='...',
                            descricao='saldo inicial',
                            categoria='...',
                            created_by=request.user,
                        )          

        # update context with fresh data when a new bank is created
        company = request.user.company
        banks = BankAccount.objects.filter(company=company).order_by('-saldo')
        saldos: list = [bank.saldo for bank in banks]
        saldo_total: Decimal = Decimal(sum(saldos))

        context = {
            'bank_account_form': form,
            'saldo_total': saldo_total,
            'banks': banks,
        }

        # merge additional transaction data
        context.update(Finance.get_transactions_by_date(request))

        return context

    @staticmethod
    def edit_bank_account(request) -> dict[str, object]:
        edit_bank_form = BankAccountForm()
        post_data = request.POST.copy()

        if saldo := post_data.get('saldo', ''):
            try:
                saldo_cleaned = Decimal(saldo.replace('.', '').replace(',', '.'))
                post_data['saldo'] = saldo_cleaned
            except InvalidOperation:
                raise ValueError("invalid monetary value format")            
            
        if request.method == 'POST' and 'edit-account' in request.POST:
            bank_id = post_data['id']
            bank = BankAccount.objects.get(id=bank_id)
            edit_bank_form = BankAccountForm(post_data, instance=bank)
            if edit_bank_form.is_valid():
                edit_bank_form.save()
            else:
                print(edit_bank_form.errors)

        return {'edit_bank_form': edit_bank_form}
