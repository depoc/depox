from django.contrib import admin

from .models import BankAccount, Transactions


class TransactionsInline(admin.StackedInline):
    model = Transactions
    extra = 0
    ordering = ('-created',)  


class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'saldo')
    inlines = [TransactionsInline]


class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'valor', 'conta', 'created')
    ordering = ['-created']
    readonly_fields = ('conta', 'created_by', 'created')


admin.site.register(BankAccount, BankAccountAdmin)
admin.site.register(Transactions, TransactionsAdmin)