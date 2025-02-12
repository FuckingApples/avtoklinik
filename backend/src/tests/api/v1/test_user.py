import pytest


@pytest.mark.django_db
def test_user_registration(api_client):
    payload = dict(
        first_name="John",
        last_name="Doe",
        email="johndoe@example.com",
        password="qwerty",
    )
    response = api_client.post("/api/v1/users/register", data=payload)

    data = response.data
    assert data["email"] == payload["email"]
    assert data["first_name"] == payload["first_name"]
    assert data["last_name"] == payload["last_name"]
    assert "password" not in data
    assert response.status_code == 201


@pytest.mark.django_db
def test_user_registration_with_existing_email(user, api_client):
    payload = dict(
        first_name="Bob",
        last_name="Robinson",
        email="bobrobinson@example.com",
        password="simplepassword",
    )
    response = api_client.post("/api/v1/users/register", data=payload)

    assert response.status_code == 400
