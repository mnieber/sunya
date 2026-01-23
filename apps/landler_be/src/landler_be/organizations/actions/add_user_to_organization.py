from dataclassy import dataclass
from django.contrib.auth import get_user_model

from organizations.enums import UserInOrganizationRoles
from organizations.models import Organization, OrganizationMembership

User = get_user_model()


@dataclass
class AddUserToOrganizationForm:
    display_name: str
    member_email: str
    role: UserInOrganizationRoles


def add_user_to_organization(
    add_user_to_organization_form, organization: Organization, user: User
):
    _validate_args(add_user_to_organization_form, organization, user)

    membership = OrganizationMembership(
        organization=organization,
        user=user,
        role=add_user_to_organization_form.role,
        display_name=add_user_to_organization_form.display_name,
        member_email=add_user_to_organization_form.member_email,
    )
    membership.save()

    return membership


def _validate_args(
    add_user_to_organization_form, organization: Organization, user: User
):
    if OrganizationMembership.objects.filter(
        organization=organization, user=user
    ).exists():
        raise UserAlreadyInOrganizationError()

    if add_user_to_organization_form.role not in UserInOrganizationRoles.values:
        raise InvalidRoleError()


class UserAlreadyInOrganizationError(Exception):
    pass


class InvalidRoleError(Exception):
    pass
