from django.contrib import admin

from .models import BankAccount, Transactions


class TransactionsInline(admin.StackedInline):
    model = Transactions
    extra = 0
    ordering = ('-created',)

    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     return qs.filter(tipo='receber')    


class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'saldo')
    inlines = [TransactionsInline]


class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'valor', 'conta', 'created')

admin.site.register(BankAccount, BankAccountAdmin)
admin.site.register(Transactions, TransactionsAdmin)