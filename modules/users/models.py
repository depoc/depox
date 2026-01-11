from django.db import models
from django.contrib.auth.models import AbstractUser

from modules.erp.models import Company

from .managers import UserManager


class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True, blank=True)
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        null=True, blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager() # type: ignore

    def __str__(self):
        return self.name

