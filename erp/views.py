from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from users.forms import CustomUserChangeForm
from .forms import CompanyForm


class Settings:
    def user(request) -> dict:
        user = request.user
        form = CustomUserChangeForm(instance=user)

        if request.method == 'POST':
                if 'user-form' in request.POST:
                    form = CustomUserChangeForm(request.POST, instance=user)
                    if form.is_valid():
                        form.save()

        context = {'form': form}
        return context
    

    class PasswordChange(PasswordChangeView):
        template_name = 'erp/partials/_password.html'
        success_url = reverse_lazy('erp:index')

    def company(request) -> dict:
        user = request.user
        company = user.company
        form = CompanyForm(instance=company)

        if request.method == 'POST':
            if 'company-form' in request.POST:
                form = CompanyForm(request.POST, instance=company)
                if form.is_valid():
                    company = form.save()
                    user.company = company
                    user.save()

        context = {'company_form': form}
        return context


@login_required(login_url='users:login')
def erp(request):
    context = Settings.user(request)
    context.update(Settings.company(request))

    return render(request, 'erp/index.html', context)


@login_required(login_url='users:login')
def delete(request):
    user = request.user
    company = user.company

    if request.method == 'POST':
        if company:
            company.delete()
        else:
            user.delete()
            
        return redirect('users:register')