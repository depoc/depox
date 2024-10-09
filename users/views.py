from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.shortcuts import render, redirect

from .models import User
from .forms import (
    CustomUserCreationForm,
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
    return render(request, 'users/signIn.html', context)

