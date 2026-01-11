from django.forms import ModelForm, ChoiceField

from .models import Transactions, BankAccount, Categories
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

        category_groups = Categories.objects \
            .filter(is_group=True, is_active=True) \
            .order_by('-nome') \

        subcategories = Categories.objects \
            .filter(is_group=False, is_active=True) \
            .order_by('nome')

        categorias = {}
        for group in category_groups:
            categorias[group.nome] = {'subcategorias': []}

        for sub in subcategories:
            categorias[sub.parent.nome]['subcategorias'].append({'nome': sub.nome, 'id': str(sub.id)})

        self.category = categorias
        
        self.fields['conta'].empty_label = 'escolha conta'
        self.fields['contato'].empty_label = 'escolha contato'
        self.fields['categoria'].empty_label = 'escolha categoria'

        for _, field in self.fields.items():
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


class CategoriesForm(ModelForm):
    class Meta:
        model = Categories
        fields = ["nome", "parent"]
