from rest_framework import serializers

from deals.apps.processor.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ("name",)

