from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from erp.services import Settings

@login_required(login_url='users:login')
def caixa(request):
    context = Settings.context(request)
    return render(request, 'finance/caixa.html', context)