from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from erp.services import Settings
from .services import Finance


@login_required(login_url='users:login')
def caixa(request):
    context = Settings.context(request)
    context.update(Finance.context(request))

    return render(request, 'finance/caixa.html', context)


@login_required(login_url='users:login')
def transaction(request):
    context = Finance.context(request)
    return render(request, 'finance/common/_transaction.html', context)