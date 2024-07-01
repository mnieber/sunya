from django.contrib.auth import get_user_model
from organizations.models import Organization

User = get_user_model()


def add_user_to_organization(user: User, organization: Organization):
    _validate_args(user, organization)

    organization.users.add(user)
    organization.save()


def _validate_args(user, organization):
    if user in organization.users.all():
        raise UserAlreadyInOrganizationError()


class UserAlreadyInOrganizationError(Exception):
    pass
