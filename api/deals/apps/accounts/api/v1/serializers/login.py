from django.contrib.auth import authenticate as django_authenticate
from django.utils.translation import gettext

from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField(write_only=True, max_length=254)
    password = serializers.CharField(max_length=128, style={"input_type": "password"}, write_only=True)

    @staticmethod
    def _authenticate(username, password):
        return django_authenticate(username=username, password=password)  # pragma: no cover

    def validate(self, attrs):
        user = self._authenticate(attrs.get("username"), attrs.get("password"))
        if user:
            return {"user": user}
        raise ValidationError(gettext("Incorrect username or password."))

    def create(self, validated_data):
        assert False, "Do not use update directly"  # nosec

    def update(self, instance, validated_data):
        assert False, "Do not use update directly"  # nosec
