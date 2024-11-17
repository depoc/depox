from .models import BankAccount
from .forms import TransactionsForm


class Finance:
    @staticmethod
    def context(request) -> dict:
        context = {}
        context.update(Finance.get_balance_context(request))
        context.update(Finance.add_transactions(request))

        return context


    @staticmethod
    def get_balance_context(request) -> dict:
        company = request.user.company
        banks = BankAccount.objects.filter(company=company)

        saldos = [bank.saldo for bank in banks]
        saldo_total = sum(saldos)
        
        return {'saldo_total': saldo_total, 'banks': banks}
    

    @staticmethod
    def add_transactions(request) -> dict:
        form = TransactionsForm

        if request.method == 'POST' and 'add-transaction' in request.POST:
                form = TransactionsForm(request.POST)
                if form.is_valid():
                     form.save()

        return {'transaction': form}