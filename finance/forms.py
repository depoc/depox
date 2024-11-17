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
                    placeholder:text-black/40 dark:placeholder:text-white/50
                    appearance-none w-full sm:w-1/2 text-center
                    bg-transparent
                    outline-none''',
            })            
