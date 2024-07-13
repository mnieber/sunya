from api.utils.extend_schema import allow, deny
from organizations.enums import UserInOrganizationRoles
from organizations.models import OrganizationMembership


def user_is_organization_admin(user, organization):
    if user.is_anonymous:
        return deny("User must be authenticated")

    try:
        membership = OrganizationMembership.objects.get(
            user=user, organization=organization
        )
        if membership.role == UserInOrganizationRoles.ADMIN:
            return allow()
    except OrganizationMembership.DoesNotExist:
        pass
    return deny("User must be an admin of the organization")


def user_is_organization_member(user, organization):
    if user.is_anonymous:
        return deny("User must be authenticated")

    if OrganizationMembership.objects.filter(
        user=user, organization=organization
    ).exists():
        return allow()
    return deny("User must be a member of the organization")
