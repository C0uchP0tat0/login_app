from django.db import models
from djmoney.models.fields import MoneyField
from django.contrib.auth.models import User


class Wallet(models.Model):
    balance = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
