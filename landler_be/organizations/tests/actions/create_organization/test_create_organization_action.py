import pytest

from organizations.actions.create_organization import (
    CreateOrganizationForm,
    OrganizationWithNameAlreadyExistsError,
    create_organization,
)
from organizations.tests.factories import OrganizationFactory


class TestCreateOrganizationAction:
    @pytest.mark.django_db
    def test_create_organization_success(self):
        # Given
        create_organization_form = CreateOrganizationForm(name="Test Organization")

        # When
        organization = create_organization(create_organization_form)

        # Then
        assert organization.name == "Test Organization"

    @pytest.mark.django_db
    def test_create_organization_with_existing_name(self):
        # Given
        OrganizationFactory(name="Existing Organization")
        create_organization_form = CreateOrganizationForm(name="Existing Organization")

        # When / Then
        with pytest.raises(OrganizationWithNameAlreadyExistsError):
            create_organization(create_organization_form)
