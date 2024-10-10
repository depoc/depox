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
                form = CustomUserChangeForm(request.POST, instance=user)
                if form.is_valid():
                    form.save()

        context = {'form': form}
        return context



@login_required(login_url='users:login')
def erp(request):
    context = Settings.user(request)

    return render(request, 'erp/index.html', context)


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'erp/partials/_password.html'
    success_url = reverse_lazy('erp:index')