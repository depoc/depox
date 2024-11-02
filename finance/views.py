from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from erp.services import Settings
from .models import BankAccount

@login_required(login_url='users:login')
def caixa(request):
    company = request.user.company
    banks = BankAccount.objects.filter(company=company)
    saldos = []
    for bank in banks:
        saldos.append(bank.saldo)
    saldo_total = sum(saldos)
    
    context:dict = Settings.context(request)
    context.update({'saldo_total': saldo_total})
    return render(request, 'finance/caixa.html', context)