import pytest
from organizations.actions.add_user_to_organization import (
    UserAlreadyInOrganizationError,
    add_user_to_organization,
)


class TestAddUserToOrganizationAction:
    @pytest.mark.django_db
    def test_add_user_to_organization_success(self, user_factory, organization_factory):
        # Given
        user = user_factory()
        organization = organization_factory()

        # When
        add_user_to_organization(organization=organization, user=user)

        # Then
        assert organization.users.filter(id=user.id).exists()

    @pytest.mark.django_db
    def test_add_user_to_organization_with_user_already_in_organization(
        self, user_factory, organization_factory
    ):
        # Given
        user = user_factory()
        organization = organization_factory()
        organization.users.add(user)

        # When
        with pytest.raises(UserAlreadyInOrganizationError):
            add_user_to_organization(organization=organization, user=user)
