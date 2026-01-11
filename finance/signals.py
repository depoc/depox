from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db import transaction
from django.db.models import Sum

from erp.models import Company
from .models import BankAccount, Transactions, Categories


@receiver(post_save, sender=Company)
def create_bank_account(sender, instance, created, **kwargs):
    if created:
        BankAccount.objects.create(
            nome = 'caixa',
            company=instance,
        )

@receiver(post_save, sender=Company)
def create_finance_categories(sender, instance, created, **kwargs):
    if created:
        receitas, _ = Categories.objects.get_or_create(
            nome="receitas", is_group=True
        )
        despesas, _ = Categories.objects.get_or_create(
            nome="despesas", is_group=True
        )

        categories = [
            Categories(nome="vendas", parent=receitas),
            Categories(nome="outras receitas", parent=receitas),
            Categories(nome="aluguel", parent=despesas),
            Categories(nome="água, luz", parent=despesas),
            Categories(nome="internet, celular", parent=despesas),
            Categories(nome="mercadorias, insumos", parent=despesas),
            Categories(nome="salários", parent=despesas),
            Categories(nome="marketing e publicidade", parent=despesas),
            Categories(nome="transporte/fretes", parent=despesas),
            Categories(nome="serviços gerais", parent=despesas),
            Categories(nome="manutenção e reparos", parent=despesas),
            Categories(nome="equipamentos", parent=despesas),
            Categories(nome="despesas financeiras", parent=despesas),
        ]
        Categories.objects.bulk_create(categories)

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