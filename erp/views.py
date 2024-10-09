from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from users.forms import CustomUserChangeForm

class Settings:
    def user(request) -> dict:
        user = request.user
        form = CustomUserChangeForm(instance=user)

        if request.method == "POST":
            form = CustomUserChangeForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return redirect('erp:index')

        context = {'form': form}
        return context


@login_required(login_url='users:login')
def erp(request):
    context = Settings.user(request)

    return render(request, 'erp/index.html', context) 