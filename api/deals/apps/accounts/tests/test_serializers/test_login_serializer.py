from rest_framework.exceptions import ValidationError

import pytest

from deals.apps.accounts.api.v1.serializers.login import LoginSerializer


@pytest.mark.django_db
def test_login_serializer_validate_success(user_account):
    username = "jack"
    password = "super_secret_password"  # nosec
    user = user_account(username=username)
    user.set_password(password)
    user.save(update_fields=("password",))
    serializer = LoginSerializer()

    result = serializer.validate({"username": username, "password": password})
    assert result == {"user": user}


@pytest.mark.django_db
def test_login_serializer_validate_failure(user_account):
    username = "jane"
    password = "super_secret_password"  # nosec
    user = user_account(username=username)
    user.set_password(password)
    user.save(update_fields=("password",))
    serializer = LoginSerializer()

    with pytest.raises(ValidationError):
        serializer.validate({"username": username, "password": "incorrect"})
