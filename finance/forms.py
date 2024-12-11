from django.forms import ModelForm

from .models import Transactions, BankAccount
from contacts.models import Contacts


class TransactionsForm(ModelForm):
    class Meta:
        model = Transactions
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        company = kwargs.pop('company')
        super(TransactionsForm, self).__init__(*args, **kwargs)

        self.fields['conta'].queryset = BankAccount.objects \
            .filter(company=company) \
            .order_by('-saldo')
        
        self.fields['contato'].queryset = Contacts.objects \
            .filter(company=company) \
            .order_by('nome')
        
        self.fields['conta'].empty_label = None
        self.fields['contato'].empty_label = 'escolha contato'

        for name, field in self.fields.items():
            field.widget.attrs.update({
                'autofocus': True,
                'class': '''
                    placeholder:text-black dark:placeholder:text-white
                    appearance-none w-full
                    bg-transparent
                    outline-none''',
            })            


class BankAccountForm(ModelForm):
    class Meta:
        model = BankAccount
        fields = '__all__'