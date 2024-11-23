from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect

from erp.services import Settings
from .services import Finance

from .models import Transactions, BankAccount


def has_company(user):
    return hasattr(user, 'company') and user.company is not None

@user_passes_test(has_company, login_url='users:login')
def caixa(request):
    context = Settings.context(request)
    context.update(Finance.context(request))

    return render(request, 'finance/caixa.html', context)

@login_required(login_url='users:login')
def delete_transaction(request, pk):
    transaction = Transactions.objects.get(pk=pk)

    if request.method == 'POST':
        transaction.delete()

    return redirect('finance:caixa') 

@login_required
def delete_bank(request, pk):
    bank = BankAccount.objects.get(pk=pk)
    transactions = Transactions.objects.filter(conta=bank)

    if request.method == 'POST' and 'delete-bank' in request.POST:
        if not transactions:
            bank.delete()
        else:
            print('banco possui lançamentos, para')

    return redirect('finance:caixa')