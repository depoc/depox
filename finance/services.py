from django.shortcuts import redirect
from .models import BankAccount
from .forms import TransactionsForm


class Finance:
    @staticmethod
    def context(request) -> dict:
        """
        Gera o contexto geral para as views relacionadas a finanças.
        """
        context = {}
        context.update(Finance.add_transactions(request))
        return context

    @staticmethod
    def add_transactions(request) -> dict:
        """
        Lida com a lógica de adicionar transações e calcula o saldo total das contas bancárias.
        """
        form = TransactionsForm()
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
        post_data['valor'] = valor_cleaned

        if tipo == 'entrada':
            saldo = float(bank.saldo) + float(valor_cleaned)
            bank.saldo = saldo
            bank.save()

        form = TransactionsForm(post_data)
        if form.is_valid():
            form.save()

        return form
