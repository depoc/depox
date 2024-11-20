from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db import transaction
from django.db.models import Sum

from erp.models import Company
from .models import BankAccount, Transactions


@receiver(post_save, sender=Company)
def create_bank_account(sender, instance, created, **kwargs):
    if created:
        BankAccount.objects.create(
            name = 'caixa',
            company=instance,
        )

@receiver(post_save, sender=Transactions)
def update_bank_account_balance(sender, instance, **kwargs):
    with transaction.atomic():
        bank_account = instance.conta
        total_debit = Transactions.objects.filter(conta=bank_account).aggregate(Sum('valor'))['valor__sum'] or 0
        bank_account.saldo = total_debit
        bank_account.save()        

@receiver(post_delete, sender=Transactions)
def update_bank_account_balance_on_delete(sender, instance, **kwargs):
    # Inicia uma transação para garantir que tudo seja atômico
    with transaction.atomic():
        bank_account = instance.conta
        # Recalculate the total balance for the bank account after the transaction is deleted
        total_debit = Transactions.objects.filter(conta=bank_account).aggregate(Sum('valor'))['valor__sum'] or 0
        bank_account.saldo = total_debit
        bank_account.save()        

@receiver(post_save, sender=Transactions)
def link_transfer_transaction(sender, instance, created, **kwargs):
    linked_transaction = instance.linked
    if created and linked_transaction:
        linked_transaction.linked = instance
        linked_transaction.save()