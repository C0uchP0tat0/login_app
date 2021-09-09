from django.db import models
from django.contrib.auth.models import User


class Wallet(models.Model):
    balance = models.DecimalField(max_digits=7, decimal_places=2)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
