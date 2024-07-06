from django.contrib.auth import get_user_model

from organizations.enums import UserInOrganizationRoles
from organizations.models import Organization, OrganizationMembership

User = get_user_model()


def add_user_to_organization(
    organization: Organization, user: User, role: UserInOrganizationRoles
):
    _validate_args(organization, user, role)

    membership = OrganizationMembership(organization=organization, user=user, role=role)
    membership.save()

    return membership


def _validate_args(
    organization: Organization, user: User, role: UserInOrganizationRoles
):
    if OrganizationMembership.objects.filter(
        organization=organization, user=user
    ).exists():
        raise UserAlreadyInOrganizationError()

    if role not in UserInOrganizationRoles.values:
        raise InvalidRoleError()


class UserAlreadyInOrganizationError(Exception):
    pass


class InvalidRoleError(Exception):
    pass
