from django.contrib import admin

from .models import BankAccount


class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'saldo')

admin.site.register(BankAccount, BankAccountAdmin)