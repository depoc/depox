from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import Company

from users.models import User


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({
                'autofocus': True,
                'placeholder': '...',
                'class': '''
                    w-fit
                    text-xs
                    text-end
                    bg-transparent
                    text-black/40
                    dark:text-white/40
                    outline-none''',
            })    


class MemberCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'email',
            'name',
            'username',
        ]

    def __init__(self, *args, **kwargs):
        super(MemberCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({
                'autofocus': True,
                'placeholder': '...',
                'class': '''
                    w-fit
                    text-xs
                    text-end
                    bg-transparent
                    text-black/40
                    dark:text-white/40
                    outline-none''',
            })    


    def save(self, commit=True):
        user = super().save(commit=False)
        if user.username:
            user.username = user.username.lower()
        if commit:
            user.save()
        return user                