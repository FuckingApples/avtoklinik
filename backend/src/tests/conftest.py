import pytest
from apps.api.serializers.users import UserDTO
from apps.users.services import create
from rest_framework.test import APIClient


@pytest.fixture
def user():
    user_dto = UserDTO(
        first_name="Bob",
        last_name="Robinson",
        email="bobrobinson@example.com",
        password="simplepassword",
    )

    user = create.create_user(user_dto)
    return user


@pytest.fixture
def api_client():
    return APIClient()
