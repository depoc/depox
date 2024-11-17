from django.forms import ModelForm

from .models import Transactions


class TransactionsForm(ModelForm):
    class Meta:
        model = Transactions
        fields = '__all__'