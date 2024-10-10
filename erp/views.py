from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from users.forms import CustomUserChangeForm

class Settings:
    def user(request) -> dict:
        user = request.user
        form = CustomUserChangeForm(instance=user)

        if request.method == 'POST':
            if 'form' in request.POST:
                form = CustomUserChangeForm(request.POST, instance=user)
                if form.is_valid():
                    form.save()

        context = {'form': form}
        return context
    
    def password(request):
        user = request.user
        password_change_form = PasswordChangeForm

        if request.method == 'POST':
            if 'password_change_form' in request.POST:
                password_change_form = PasswordChangeForm(user=user)
                if password_change_form.is_valid():
                    password_change_form.save()
                else:
                    print(password_change_form.errors)

        context = {'password_change_form': password_change_form}
        return context


@login_required(login_url='users:login')
def erp(request):
    context = Settings.user(request)
    context.update(Settings.password(request))

    return render(request, 'erp/index.html', context)


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'erp/partials/_password.html'
    success_url = reverse_lazy('erp:index')