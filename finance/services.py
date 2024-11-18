from django.db.models import Q
from django.utils.timezone import now

from .models import BankAccount, Transactions
from .forms import TransactionsForm


class Finance:
    @staticmethod
    def context(request) -> dict:
        """
        Gera o contexto geral para as views relacionadas a finanças.
        """
        context = {}
        context.update(Finance.add_transactions(request))
        context.update(Finance.get_cash_flow(request))
        return context

    @staticmethod
    def add_transactions(request) -> dict:
        """
        Lida com a lógica de adicionar transações e calcula o saldo total das contas bancárias.
        """
        form = TransactionsForm(user=request.user)
        conta = request.POST.get('conta')
        tipo = request.POST.get('tipo')

        if conta:
            bank = BankAccount.objects.get(id=conta)

        if request.method == 'POST' and 'add-transaction' in request.POST:
            form = Finance._process_transaction(request, form, bank, tipo)

        # Dados da empresa e bancos
        company = request.user.company
        banks = BankAccount.objects.filter(company=company)

        # Cálculo do saldo total
        saldo_total = sum(bank.saldo for bank in banks)

        return {'transaction': form, 'saldo_total': saldo_total, 'banks': banks}

    @staticmethod
    def _process_transaction(request, form, bank, tipo) -> TransactionsForm:
        """
        Processa uma transação, atualiza o saldo do banco e salva o formulário de transação.
        """
        post_data = request.POST.copy()
        valor = post_data.get('valor', '')
        valor_cleaned = valor.replace('.', '').replace(',', '.')

        if tipo == 'receber':
            valor = float(valor_cleaned)
            post_data['valor'] = valor

        if tipo == 'pagar':
            valor = float(valor_cleaned) * (-1)
            post_data['valor'] = valor

        form = TransactionsForm(post_data, user=request.user)
        if form.is_valid():
            form.save()

        return form

    @staticmethod
    def get_cash_flow(request) -> dict:
        company = request.user.company
        banks = BankAccount.objects.filter(company=company)
        transactions = Transactions.objects \
            .filter(conta__in=banks) \
            .order_by('-created')

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
            'transactions': transactions,
            'pagamentos': pagamentos,
            'recebimentos': recebimentos,
            'balanco': balanco,
            'current_date': now,
        }    
    
