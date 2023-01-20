from django.utils.translation import gettext

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from deals.apps.accounts.exceptions import InvalidPasswordError
from deals.apps.accounts.models import UserAccount
from deals.apps.accounts.services.password import PasswordService


class RegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True, max_length=128)
    password = serializers.CharField(write_only=True, max_length=128)
    first_name = serializers.CharField(required=True, max_length=30)
    last_name = serializers.CharField(required=True, max_length=30)

    class Meta:
        model = UserAccount
        fields = ("username", "first_name", "last_name", "password")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.password_service = PasswordService()

    def validate_username(self, username):
        if UserAccount.objects.filter(username=username).exists():
            raise ValidationError(gettext("Could not create account with this username."))
        return super().validate(username)

    def validate_password(self, new_password):
        try:
            self.password_service.validate_password(new_password)
        except InvalidPasswordError as e:
            raise serializers.ValidationError(e.messages) from e
        return new_password

    def save(self, **kwargs):
        self.instance = super().save(**kwargs)
        raw_password = self.validated_data.get("password")
        self.instance.set_password(raw_password)
        self.instance.save()
        return self.instance
