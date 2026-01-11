from django.contrib import admin

from .models import BankAccount, Transactions, Categories


class TransactionsInline(admin.StackedInline):
    model = Transactions
    extra = 0
    ordering = ('-created',)  


class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('nome', 'company', 'saldo')
    inlines = [TransactionsInline]


class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'valor', 'conta', 'created')
    ordering = ['-created']
    readonly_fields = ('conta', 'created_by', 'created')


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['nome']
    readonly_fields = ['id']


admin.site.register(BankAccount, BankAccountAdmin)
admin.site.register(Transactions, TransactionsAdmin)
admin.site.register(Categories, CategoriesAdmin)