from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from users.forms import CustomUserChangeForm


@login_required(login_url='login')
def erp(request):
    user = request.user
    form = CustomUserChangeForm(instance=user)

    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('erp:index')

    context = {'form': form}

    return render(request, 'erp/index.html', context) 