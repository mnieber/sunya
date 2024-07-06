import pytest
from django.contrib.auth import get_user_model

from organizations.enums import UserInOrganizationRoles
from organizations.permissions import user_is_organization_member
from organizations.tests.factories import (
    OrganizationFactory,
    OrganizationMembershipFactory,
)
from users.tests.factories import UserFactory

User = get_user_model()


class TestUserIsOrganizationMemberPermission:

    @pytest.fixture
    def organization(self):
        return OrganizationFactory()

    @pytest.fixture
    def user(self):
        return UserFactory()

    @pytest.mark.django_db
    def test_user_is_organization_member_success(self, organization, user):
        OrganizationMembershipFactory(
            organization=organization, user=user, role=UserInOrganizationRoles.EDITOR
        )

        result = user_is_organization_member(user, organization)

        assert result.permission_allowed
        assert result.reason is None

    @pytest.mark.django_db
    def test_user_is_organization_member_success_as_admin(self, organization, user):
        OrganizationMembershipFactory(
            organization=organization, user=user, role=UserInOrganizationRoles.ADMIN
        )

        result = user_is_organization_member(user, organization)

        assert result.permission_allowed
        assert result.reason is None

    @pytest.mark.django_db
    def test_user_is_organization_member_failure(self, organization, user):
        result = user_is_organization_member(user, organization)

        assert not result.permission_allowed
        assert result.reason == "User must be a member of the organization"
