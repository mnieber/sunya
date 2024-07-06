import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from organizations.tests.factories import (
    OrganizationFactory,
    OrganizationMembershipFactory,
)
from users.tests.factories import UserFactory


class TestSetActiveOrganizationApiView:
    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.fixture
    def user(self):
        return UserFactory()

    @pytest.fixture
    def organization(self):
        return OrganizationFactory()

    @pytest.mark.django_db
    def test_set_active_organization_success(self, api_client, user, organization):
        # Given
        OrganizationMembershipFactory(user=user, organization=organization)
        api_client.force_authenticate(user=user)
        url = reverse(
            "set-active-organization", kwargs={"organization_id": organization.id}
        )

        # When
        response = api_client.post(url)

        # Then
        assert response.status_code == status.HTTP_200_OK
        assert response.data["id"] == str(organization.id)
        assert response.data["name"] == organization.name

        # Check if the active organization is set in the session
        assert api_client.session["active_organization_id"] == str(organization.id)

    @pytest.mark.django_db
    def test_set_active_organization_not_member(self, api_client, user, organization):
        # Given
        api_client.force_authenticate(user=user)
        url = reverse(
            "set-active-organization", kwargs={"organization_id": organization.id}
        )

        # When
        response = api_client.post(url)

        # Then
        assert response.status_code == status.HTTP_403_FORBIDDEN

    @pytest.mark.django_db
    def test_set_active_organization_unauthenticated(self, api_client, organization):
        # Given
        url = reverse(
            "set-active-organization", kwargs={"organization_id": organization.id}
        )

        # When
        response = api_client.post(url)

        # Then
        assert response.status_code == status.HTTP_403_FORBIDDEN

    @pytest.mark.django_db
    def test_set_active_organization_not_found(self, api_client, user):
        # Given
        api_client.force_authenticate(user=user)
        url = reverse(
            "set-active-organization",
            kwargs={"organization_id": "00000000-0000-0000-0000-000000000000"},
        )

        # When
        response = api_client.post(url)

        # Then
        assert response.status_code == status.HTTP_404_NOT_FOUND
