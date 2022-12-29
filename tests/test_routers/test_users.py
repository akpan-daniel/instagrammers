from fastapi import status
from fastapi.testclient import TestClient

from app.config.settings import get_settings

settings = get_settings()


def test_create_user(client: TestClient):
    data = {
        "email": settings.test_user_email,
        "password": settings.test_user_password,
    }
    response_obj = client.post("/api/users/", json=data)

    response = response_obj.json()

    assert response_obj.status_code == status.HTTP_200_OK
    assert "token" in response
    assert "user" in response


def test_create_bad_user(client: TestClient):
    data = {"email": settings.test_user_email}
    response_obj = client.post("/api/users/", json=data)

    assert response_obj.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    data = {"password": settings.test_user_password}
    response_obj = client.post("/api/users/", json=data)

    assert response_obj.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_list_users(client: TestClient):
    response_obj = client.get("/api/users/search")

    assert response_obj.status_code == status.HTTP_200_OK
