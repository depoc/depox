from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django import forms

from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'email',
            'name',
        ]
        labels = {
            'email': 'e-mail',
            'name': 'nome'
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password2'].label = 'confirmar senha'

        for name, field in self.fields.items():
            field.widget.attrs.update({
                'autofocus': True,
                'placeholder': name,
                'class': 
                ''' peer h-8 w-64 p-0 border-none bg-transparent
                    placeholder-transparent focus:border-transparent
                    focus:outline-none focus:ring-0 sm:text-sm ''',
            })


class CustomUserChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = [
            'email',
            'name',
            'username'
        ]
        labels = {
            'email': 'e-mail',
            'name': 'nome',
            'username': 'nome de usuário',
        }
    

    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({
                'placeholder': name,
                'class': 
                ''' peer h-8 w-64 p-0 border-none bg-transparent
                    placeholder-transparent focus:border-transparent
                    focus:outline-none focus:ring-0 sm:text-sm ''',
            })    


class CustomPasswordChangeForm(PasswordChangeForm):
    fields = [
        ('old_password', 'senha antiga'),
        ('new_password1', 'nova senha'),
        ('new_password2', 'confirmar nova senha'),
    ]

    for name, label in fields:
        locals()[name] = forms.CharField(
            label=(label),
            strip=False,
            widget=forms.PasswordInput(
                attrs={
                    'autofocus': True,
                    'placeholder': label,
                    'autocomplete': 'current-password' \
                        if name == 'old_password' else 'off',
                    'class': 
                    ''' peer h-8 w-64 p-0 border-none bg-transparent
                        placeholder-transparent focus:border-transparent
                        focus:outline-none focus:ring-0 sm:text-sm ''',
                }
            ),
        )

