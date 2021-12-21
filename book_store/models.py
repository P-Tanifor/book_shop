from django.db import models
from django.contrib.auth.models import User
import django


class AvailableBooks(models.Model):
    book_title = models.CharField(max_length=1024)
    quantity = models.IntegerField()
    inventory_date = models.DateField()


class ConfirmedOrders(models.Model):
    book_title = models.CharField(max_length=1024)
    ordered_by = models.ForeignKey(django.contrib.auth.models.User, on_delete=models.CASCADE)
    ordered_qty = models.IntegerField()

