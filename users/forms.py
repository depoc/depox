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
            'email': 'email',
            'name': 'nome',
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password2'].label = 'confirme senha'

        for name, field in self.fields.items():
            field.widget.attrs.update({
                'autofocus': True,
                'placeholder': field.label.lower(),
                'class': 
                ''' w-full
                    p-2
                    text-xs
                    bg-transparent
                    outline-none
                    placeholder:text-white/60
                    text-black/80 dark:text-white/60''',
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
            'name': 'nome',
            'username': 'usuário',
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({
                'class': '''
                    w-full
                    text-xs
                    text-end
                    bg-transparent
                    text-black/40
                    dark:text-white/40
                    outline-none''',
            })