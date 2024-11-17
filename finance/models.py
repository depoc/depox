from django.db import models

from erp.models import Company


class BankAccount(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='banks',
    )
    name = models.CharField(max_length=255)
    agencia = models.CharField(max_length=255, blank=True, null=True)
    conta = models.CharField(max_length=255, blank=True, null=True)
    saldo = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True, default=0,
    )

    def __str__(self):
        return f'{self.name}'


class Transactions(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=255, blank=True, null=True)
    valor = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True,
    )
    conta = models.ForeignKey(BankAccount, on_delete=models.CASCADE, default='conta')
    contato = models.CharField(max_length=255, blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=False, null=False)
    categoria = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'entrada {self.valor} - {self.conta}' 