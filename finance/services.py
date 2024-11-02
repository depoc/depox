from .models import BankAccount


class Finance:
    @staticmethod
    def context(request) -> dict:
        context = {}
        context.update(Finance.get_balance_context(request))

        return context


    @staticmethod
    def get_balance_context(request) -> dict:
        company = request.user.company
        banks = BankAccount.objects.filter(company=company)

        saldos = [bank.saldo for bank in banks]
        saldo_total = sum(saldos)
        
        return {'saldo_total': saldo_total}