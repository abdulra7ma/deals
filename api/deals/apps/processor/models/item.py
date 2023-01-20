from django.db import models
from deals.apps.common.models import CoreModel


class Item(models.Model):
    name = models.CharField(
        max_length=255, unique=True, blank=False, null=False
    )
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-name"]
        verbose_name = "Item"
        verbose_name_plural = "Items"
