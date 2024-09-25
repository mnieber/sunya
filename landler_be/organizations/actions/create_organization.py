from dataclassy import dataclass
from django.contrib.auth import get_user_model

from organizations.models import Organization, OrganizationStaffSettings

User = get_user_model()


@dataclass
class CreateOrganizationForm:
    name: str


def create_organization(create_organization_form: CreateOrganizationForm):
    _validate_args(create_organization_form)

    organization = Organization(
        name=create_organization_form.name,
    )
    organization.save()

    OrganizationStaffSettings.objects.create(organization=organization)

    return organization


def _validate_args(create_organization_form: CreateOrganizationForm):
    if Organization.objects.filter(name=create_organization_form.name).exists():
        raise OrganizationWithNameAlreadyExistsError()


class OrganizationWithNameAlreadyExistsError(Exception):
    pass
