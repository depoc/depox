from django.forms import ModelForm

from .models import Transactions, BankAccount


class TransactionsForm(ModelForm):
    class Meta:
        model = Transactions
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(TransactionsForm, self).__init__(*args, **kwargs)

        self.fields['conta'].queryset = BankAccount.objects.filter(company=user.company)

        for name, field in self.fields.items():
            field.widget.attrs.update({
                'autofocus': True,
                'class': '''
                    placeholder:text-black dark:placeholder:text-white
                    appearance-none w-full sm:w-1/2
                    bg-transparent
                    outline-none''',
            })            


class BankAccountForm(ModelForm):
    class Meta:
        model = BankAccount
        fields = '__all__'