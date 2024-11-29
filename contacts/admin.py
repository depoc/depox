from django.contrib import admin

from .models import Contacts


class ContactsAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf_cnpj', 'company', 'tipo')

admin.site.register(Contacts, ContactsAdmin)
