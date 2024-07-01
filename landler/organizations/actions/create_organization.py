from dataclassy import dataclass
from organizations.models import Organization


@dataclass
class CreateOrganizationForm:
    name: str


def create_organization(create_organization_form: CreateOrganizationForm):
    _validate_args(create_organization_form)

    organization = Organization(name=create_organization_form.name)
    organization.save()

    return organization


def _validate_args(create_organization_form):
    if Organization.objects.filter(name=create_organization_form.name).exists():
        raise OrganizationWithNameAlreadyExistsError()


class OrganizationWithNameAlreadyExistsError(Exception):
    pass
