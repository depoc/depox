from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

import os

from .models import Company


@receiver(post_delete, sender=Company)
def auto_delete_logo_on_delete(sender, instance, **kwargs):
    logo = instance.logo
    if logo:
        if os.path.isfile(instance.logo.path):
            os.remove(instance.logo.path)


@receiver(pre_save, sender=Company)
def auto_delete_logo_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    
    try:
        old_logo = Company.objects.get(pk=instance.pk).logo
    except Company.DoesNotExist:
        return False
    
    new_logo = instance.logo
    if not old_logo:
        pass
    elif not old_logo == new_logo:
        if os.path.isfile(old_logo.path):
            os.remove(old_logo.path)
