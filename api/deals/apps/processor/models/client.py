from django.contrib.postgres.fields import ArrayField
from django.db import models
from decimal import Decimal


class Client(models.Model):
    username = models.CharField(max_length=100)
    spent_money = models.FloatField(default=0)
    gems = ArrayField(
        models.CharField(max_length=50, blank=True), default=list
    )
    transactions = models.ManyToManyField(
        "Transaction", related_name="clients"
    )

    def __str__(self):
        return self.username + str(self.spent_money)
