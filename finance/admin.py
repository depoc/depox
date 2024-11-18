from django.contrib import admin

from .models import BankAccount, Transactions


class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'saldo')


class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'valor', 'conta', 'created')

admin.site.register(BankAccount, BankAccountAdmin)
admin.site.register(Transactions, TransactionsAdmin)