from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect

from .models import User
from .forms import CustomUserCreationForm


def signin(request):
    if request.user.is_authenticated:
        return redirect('erp:index')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
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

    context = {'form': form}
    return render(request, 'users/register.html', context)


