import typing as T

from landler.backend.modules.users import Users
from landler.backend.entities import Action, ApiView
from landler.stack.entities import Enum, Form, Module
from sunya import Entity, EntityWithId, actor_to_str


class Organizations(Module):
    class Models:
        class Organization(EntityWithId):
            name: str
            memberships: T.List["Organizations.Models.OrganizationMembership"] = []

        class OrganizationMembership(Entity):
            organization: "Organizations.Models.Organization"
            user: Users.Models.User
            role: "Organizations.Enums.UserInOrganizationRoles"

    class Actions:
        class CreateOrganization(Action):
            class Args:
                create_organization_form: Form

        class AddUserToOrganization(Action):
            class Args:
                organization: "Organizations.Models.Organization"
                user: Users.Models.User
                role: "Organizations.Enums.UserInOrganizationRoles"

    class Enums:
        class UserInOrganizationRoles(Enum):
            ADMIN = "admin"
            EDITOR = "editor"

    class ApiViews:
        class CreateOrganizationApiView(ApiView):
            pass

    class DomainEvents:
        class OrganizationCreated:
            pass

        class UserAddedToOrganization:
            pass

        class UserRemovedFromOrganization:
            pass


create_organization_action = Organizations.Actions.CreateOrganization()
create_organization_api_view = Organizations.ApiViews.CreateOrganizationApiView()
add_user_to_organization_action = Organizations.Actions.AddUserToOrganization()


@actor_to_str.method((Organizations.Models.Organization,))
def organization_to_str(organization):
    return f"{organization.name}+:organization"


@actor_to_str.method((Organizations.Models.OrganizationMembership,))
def organization_membership_to_str(organization_membership):
    return (
        f"({organization_membership.organization.name})-"
        + f"({organization_membership.user.email})-"
        + f"({organization_membership.role})+:organization-membership"
    )
