from django.db import models


# Create your models here.

class warehouse(models.Model):
    ware_name = models.CharField(max_length=50, default='unknown')
    ware_ready = models.IntegerField(default=0)
    ware_semi = models.IntegerField(default=0)

    def __str__(self):
        return self.ware_name
