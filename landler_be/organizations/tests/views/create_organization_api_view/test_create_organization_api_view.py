import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from api.utils.extend_schema.permissions import checks_permission
from common.permissions import user_is_authenticated
from organizations.views.create_organization_api_view import CreateOrganizationApiView
from users.tests.factories import UserFactory


class TestCreateOrganizationApiView:
    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.fixture
    def user(self):
        return UserFactory()

    @pytest.mark.django_db
    def test_create_organization_api_view_success(self, api_client, user):
        # Given
        api_client.force_authenticate(user=user)
        url = reverse("create-organization")
        data = {
            "create_organization_form": {
                "name": "New Organization",
            }
        }

        # When
        response = api_client.post(url, data, format="json")

        # Then
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["name"] == "New Organization"

        # Check if the user is added as an admin
        assert user.organization_memberships.filter(
            organization__name="New Organization", role="admin"
        ).exists()

    def test_create_organization_api_view_permissions(self):
        assert checks_permission(CreateOrganizationApiView.post, user_is_authenticated)
