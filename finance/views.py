from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

from erp.services import Settings
from .services import Finance


def has_company(user):
    return hasattr(user, 'company') and user.company is not None

@user_passes_test(has_company, login_url='users:login')
def caixa(request):
    context = Settings.context(request)
    context.update(Finance.context(request))

    return render(request, 'finance/caixa.html', context)
