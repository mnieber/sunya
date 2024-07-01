import pytest
from organizations.actions.create_organization import (
    CreateOrganizationForm,
    OrganizationWithNameAlreadyExistsError,
    create_organization,
)
from organizations.tests.factories import OrganizationFactory

from users.tests.factories import UserFactory


class TestCreateOrganizationAction:
    @pytest.fixture
    def owner1(self):
        return UserFactory()

    @pytest.fixture
    def owner2(self):
        return UserFactory()

    @pytest.mark.django_db
    def test_create_organization_success(self, owner1):
        # Given
        create_organization_form = CreateOrganizationForm(name="My Organization")

        # When
        organization = create_organization(create_organization_form, owner=owner1)

        # Then
        assert organization.name == create_organization_form.name

    @pytest.mark.django_db
    def test_create_organization_with_existing_name(self, owner1, owner2):
        # Given
        OrganizationFactory(name="My Organization", owner=owner1)
        create_organization_form = CreateOrganizationForm(name="My Organization")

        # When
        with pytest.raises(OrganizationWithNameAlreadyExistsError):
            create_organization(create_organization_form, owner=owner2)
