from django.db import models


# Create your models here.
class temporary_order(models.Model):
    shr = models.DecimalField(max_digits=15, decimal_places=2)
    deli = models.DecimalField(max_digits=6, decimal_places=2)
    tax = models.DecimalField(max_digits=10, decimal_places=2)


class temporary_time_address(models.Model):
    days = models.IntegerField(null=True)
    address = models.TextField(max_length=500, default='country, ...')
