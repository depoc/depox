from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect

from .models import User
from .forms import (
    CustomUserCreationForm,
    CustomUserChangeForm,
)


def signin(request):

    if request.user.is_authenticated:
        return redirect('erp:index')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, '')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('erp:index')
        else:
            messages.error(request, 'dados incorretos')

    context = {}
    return render(request, 'users/login.html', context)


def register(request):
    if request.user.is_authenticated:
        return redirect('erp:index')

    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            login(request, user)
            return redirect('erp:index')
        else:
            messages.error(request, 'dados inválidos :(')

    context = {'form': form}
    return render(request, 'users/register.html', context)


@login_required(login_url='users:login')
def delete(request):
    user = request.user

    if request.method == 'POST':
        user.delete()
        return redirect('users:register')