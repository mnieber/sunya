import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from users.tests.factories import InactiveUserFactory, UserFactory


class TestSignInUserApiView:
    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.mark.django_db
    def test_sign_in_user_success(self, api_client):
        # Given
        user = UserFactory(email="user@example.com")
        user.set_password("password123")
        user.save()

        url = reverse("sign-in-user")
        data = {
            "sign_in_user_form": {
                "email": "user@example.com",
                "password": "password123",
            }
        }

        # When
        response = api_client.post(url, data, format="json")

        # Then
        assert response.status_code == status.HTTP_200_OK
        assert response.data["email"] == "user@example.com"
        assert response.data["is_active"] == True

    @pytest.mark.django_db
    def test_sign_in_user_invalid_credentials(self, api_client):
        # Given
        UserFactory(email="user@example.com")
        url = reverse("sign-in-user")
        data = {
            "sign_in_user_form": {
                "email": "user@example.com",
                "password": "wrongpassword",
            }
        }

        # When
        response = api_client.post(url, data, format="json")

        # Then
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "non_field_errors" in response.data

    @pytest.mark.django_db
    def test_sign_in_user_inactive_user(self, api_client):
        # Given
        user = InactiveUserFactory(email="inactive@example.com")
        user.set_password("password123")
        user.save()

        url = reverse("sign-in-user")
        data = {
            "sign_in_user_form": {
                "email": "inactive@example.com",
                "password": "password123",
            }
        }

        # When
        response = api_client.post(url, data, format="json")

        # Then
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "non_field_errors" in response.data
