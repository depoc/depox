from django.contrib.auth.mixins import LoginRequiredMixin
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
def account_delete(request):
    user = request.user
    company = user.company

    if request.method == 'POST':
        if company:
            company.delete()
        else:
            user.delete()
            
    return redirect('users:register')


@login_required(login_url='users:login')
def member_delete(request, pk):
    user = User.objects.get(pk=pk)

    if request.method == 'POST' and 'member-delete' in request.POST:
        user.delete()

    return redirect('erp:index')   
    

class PasswordChange(LoginRequiredMixin, PasswordChangeView):
    template_name = 'erp/common/_password.html'
    success_url = reverse_lazy('erp:index')   
    login_url = 'users:login' 

