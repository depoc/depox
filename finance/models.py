from django.db import models

from erp.models import Company
from users.models import User
from contacts.models import Contacts

import uuid


class BankAccount(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
        )        
    created = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='banks',
    )
    nome = models.CharField(max_length=255)
    agencia = models.CharField(max_length=255, blank=True)
    conta = models.CharField(max_length=255, blank=True)
    saldo = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True, default=0,
    )

    def __str__(self):
        return f'{self.nome}'


class Transactions(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
        )        
    created = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=255, blank=False, null=False)
    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=False,
        null=False,
    )
    conta = models.ForeignKey(
        BankAccount, on_delete=models.PROTECT,
    )
    contato = models.ForeignKey(
        Contacts,
        on_delete=models.PROTECT,
        blank=True, null=True, default=None,
    )
    descricao = models.CharField(max_length=255, blank=False, null=False)
    categoria = models.CharField(max_length=255, blank=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='transactions',
    )
    linked = models.OneToOneField(
        'Transactions',
        on_delete=models.CASCADE,
        blank=True, null=True, default=None,
    )    

    def __str__(self):
        return f'{self.descricao}' 
