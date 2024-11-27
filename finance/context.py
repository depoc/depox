from decimal import Decimal

from .models import BankAccount


def processor(request):
    if request.user.is_authenticated and hasattr(request.user, 'company'):
        company = request.user.company
        banks = BankAccount.objects.filter(company=company).order_by('-saldo')
        saldos: list = [bank.saldo for bank in banks]
        saldo_total: Decimal = Decimal(sum(saldos))

        return {
            'banks': banks,
            'saldo_total': saldo_total,
        }
    
    return {}