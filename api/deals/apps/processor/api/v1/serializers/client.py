from rest_framework import serializers

from deals.apps.processor.models import Client
from .item import ItemSerializer


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ("username", "spent_money", "gems")
