import pytest

from tests.conftest import api_client


@pytest.mark.django_db
def test_obtain_token_web(api_client, user):
    payload = dict(
        email="bobrobinson@example.com",
        password="simplepassword",
    )

    response = api_client.post("/api/token", payload)
    assert "refresh" in response.cookies
    assert "access" in response.data


@pytest.mark.django_db
def test_obtain_token_mobile(api_client, user):
    payload = dict(
        email="bobrobinson@example.com",
        password="simplepassword",
    )

    response = api_client.post("/api/token", payload, headers={"User-Agent": "Mobile"})

    assert "refresh" not in response.cookies
    assert "access" in response.data
    assert "refresh" in response.data


@pytest.mark.django_db
def test_refresh_token_web(api_client, user, jwt_token):
    access_token, refresh_token = jwt_token

    response = api_client.post(
        "/api/token/refresh",
        {"refresh": refresh_token},
    )

    assert "refresh" in response.cookies
    assert "access" in response.data


@pytest.mark.django_db
def test_refresh_token_mobile(api_client, user, jwt_token):
    access_token, refresh_token = jwt_token

    response = api_client.post(
        "/api/token/refresh",
        {"refresh": refresh_token},
        headers={"User-Agent": "Mobile"},
    )

    assert "refresh" not in response.cookies
    assert "access" in response.data
    assert "refresh" in response.data
