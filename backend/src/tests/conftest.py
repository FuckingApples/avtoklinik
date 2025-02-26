import pytest
from apps.api.serializers.users import RegisterUserDTO
from apps.users.services import users
from rest_framework.test import APIClient


@pytest.fixture
def user():
    user_dto = RegisterUserDTO(
        first_name="Bob",
        last_name="Robinson",
        email="bobrobinson@example.com",
        password="simplepassword",
    )

    user = users.create_user(user_dto)
    return user


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def jwt_token(api_client):
    payload = dict(
        email="bobrobinson@example.com",
        password="simplepassword",
    )

    response = api_client.post("/api/token", payload, headers={"User-Agent": "Mobile"})

    return response.data["access"], response.data["refresh"]
