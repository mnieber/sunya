import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from api.utils.extend_schema.permissions import checks_permission
from organizations.actions.get_or_create_demo_organization import (
    get_or_create_demo_organization,
)
from organizations.models import OrganizationMembership
from users.tests.factories import UserFactory


class TestAddUserToDemoOrganizationApiView:
    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.fixture
    def user(self):
        return UserFactory()

    @pytest.fixture
    def authenticated_client(self, api_client, user):
        api_client.force_authenticate(user=user)
        return api_client

    @pytest.fixture
    def url(self):
        return reverse("add-user-to-demo-organization")

    @pytest.mark.django_db
    def test_add_user_to_demo_organization_success(
        self, authenticated_client, url, user
    ):
        # Given
        data = {
            "add_user_to_demo_organization_form": {"display_name": "Busy Blue Horse"}
        }

        # When
        response = authenticated_client.post(url, data=data, format="json")

        # Then
        assert response.status_code == status.HTTP_200_OK

        # Check if user is added to the demo organization
        membership = OrganizationMembership.objects.filter(
            organization=get_or_create_demo_organization(), user=user
        ).first()
        assert membership is not None
        assert membership.display_name == "Busy Blue Horse"
        assert membership.member_email == "busybluehorse@demo-org.com"

    @pytest.mark.django_db
    def test_add_user_to_demo_organization_unauthenticated(self, api_client, url):
        assert checks_permission
