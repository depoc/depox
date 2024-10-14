from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from users.forms import CustomUserChangeForm
from users.models import User
from .forms import CompanyForm, MemberCreationForm
from .models import Company


class Settings:
    class PasswordChange(PasswordChangeView):
        template_name = 'erp/partials/_password.html'
        success_url = reverse_lazy('erp:index')


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


    def account_delete(request):
        user = request.user
        company = user.company

        if request.method == 'POST':
            if company:
                company.delete()
            else:
                user.delete()
                
            return redirect('users:register')


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
    

    def team(request) -> dict:
        company = request.user.company
        context = {}

        if company:
            team = company.user_set.all()
            context.update({'team': team})

        return context


    def member(request) -> dict:
        company = request.user.company
        form = MemberCreationForm()

        if request.method == 'POST':
                if 'member-form' in request.POST:
                    form = CustomUserChangeForm(request.POST)
                    if form.is_valid():
                        member = form.save(commit=False)
                        member.company = company
                        member.save()

        context = {'member_form': form}
        return context
    

    def member_delete(request, pk) -> dict:
        user = User.objects.get(pk=pk)

        if request.method == 'POST':
            if 'member-delete' in request.POST:
                user.delete()

            return redirect('erp:index')   


@login_required(login_url='users:login')
def erp(request):
    context = Settings.user(request)
    context.update(Settings.company(request))
    context.update(Settings.team(request))
    context.update(Settings.member(request))

    return render(request, 'erp/index.html', context)



    
