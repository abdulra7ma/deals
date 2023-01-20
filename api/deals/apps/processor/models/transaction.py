from django.db import models

from .client import Client
from .item import Item


class Transaction(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.client.username} - {self.item.name} - {self.date}"

    class Meta:
        ordering = ["-date"]
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"
