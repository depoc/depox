from django.forms import ModelForm

from .models import Transactions


class TransactionsForm(ModelForm):
    class Meta:
        model = Transactions
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TransactionsForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({
                'autofocus': True,
                'class': '''
                    w-fit
                    placeholder:text-black/40 dark:placeholder:text-white/50
                    bg-transparent
                    outline-none''',
            })            

        if 'valor' in self.fields:
            self.fields['valor'].widget.attrs.update({'placeholder': '00,00'})            