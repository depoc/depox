from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from users.models import User

from .services import Settings    


@login_required(login_url='users:login')
def erp(request):
    context = Settings.context(request)

    return render(request, 'erp/index.html', context)


@login_required(login_url='users:login')
def account_delete(request) -> None:
    user = request.user
    company = user.company

    if request.method == 'POST':
        if company:
            company.delete()
        else:
            user.delete()
            
    return redirect('users:register')


@login_required(login_url='users:login')
def member_delete(request, pk) -> None:
    user = User.objects.get(pk=pk)

    if request.method == 'POST' and 'member-delete' in request.POST:
        user.delete()

    return redirect('erp:index')   
    

class PasswordChange(PasswordChangeView):
    template_name = 'erp/partials/_password.html'
    success_url = reverse_lazy('erp:index')    

