from django.db.models.signals import post_save
from django.dispatch import receiver

from erp.models import Company
from .models import BankAccount


@receiver(post_save, sender=Company)
def create_bank_account(sender, instance, created, **kwargs):
    if created:
        BankAccount.objects.create(
            bank = 'caixa',
            company=instance,
        )