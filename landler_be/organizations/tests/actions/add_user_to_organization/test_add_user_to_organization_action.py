import pytest

from organizations.actions.add_user_to_organization import (
    AddUserToOrganizationForm,
    InvalidRoleError,
    UserAlreadyInOrganizationError,
    add_user_to_organization,
)
from organizations.enums import UserInOrganizationRoles
from organizations.tests.factories import OrganizationFactory
from users.tests.factories import UserFactory


class TestAddUserToOrganizationAction:
    @pytest.mark.django_db
    def test_add_user_to_organization_success(self):
        # Given
        organization = OrganizationFactory()
        user = UserFactory()

        # When
        membership = add_user_to_organization(
            AddUserToOrganizationForm(
                role=UserInOrganizationRoles.ADMIN,
                display_name="Test User",
                member_email="testuser@example.org",
            ),
            organization,
            user,
        )

        # Then
        assert membership.organization == organization
        assert membership.user == user
        assert membership.role == UserInOrganizationRoles.ADMIN

    @pytest.mark.django_db
    def test_add_user_already_in_organization(self):
        # Given
        organization = OrganizationFactory()
        user = UserFactory()
        form = AddUserToOrganizationForm(
            role=UserInOrganizationRoles.EDITOR,
            display_name="Test User",
            member_email="testuser@example.org",
        )

        add_user_to_organization(
            form,
            organization,
            user,
        )

        # When / Then
        with pytest.raises(UserAlreadyInOrganizationError):
            add_user_to_organization(form, organization, user)

    @pytest.mark.django_db
    def test_add_user_with_invalid_role(self):
        # Given
        organization = OrganizationFactory()
        user = UserFactory()
        form = AddUserToOrganizationForm(
            role="invalid_role",
            display_name="Test User",
            member_email="testuser@example.org",
        )

        # When / Then
        with pytest.raises(InvalidRoleError):
            add_user_to_organization(form, organization, user)
