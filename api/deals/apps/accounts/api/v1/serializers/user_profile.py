from rest_framework import serializers

from deals.apps.accounts.models import UserAccount


class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField()

    class Meta:
        model = UserAccount
        fields = ("username", "first_name", "last_name")
