from default.stack.namespace import Module, Form, Enum
import typing as T

from landler.backend.modules.users import Users
from default.backend.namespace import Action, ApiView, Rule
from sunya import Entity, EntityWithId, actor_to_str, G as g, any_dict


class Organizations(Module):
    class Models:
        class Organization(EntityWithId):
            name: str
            memberships: T.List["Organizations.Models.OrganizationMembership"] = []

            # Related names (automatically added based on foreign keys)
            staff_settings: "Organizations.Models.OrganizationStaffSettings" = (
                any_dict()
            )

        class OrganizationMembership(Entity):
            organization: "Organizations.Models.Organization"
            user: Users.Models.User
            role: "Organizations.Enums.UserInOrganizationRoles"
            display_name: str
            member_email: str

        class OrganizationStaffSettings(EntityWithId):
            organization: "Organizations.Models.Organization"
            is_managed_by_tlg: bool
            is_demo_org: bool

    class Actions:
        class CreateOrganization(Action):
            class Args:
                create_organization_form: Form

        class AddUserToOrganization(Action):
            class Args:
                organization: "Organizations.Models.Organization"
                user: Users.Models.User
                role: "Organizations.Enums.UserInOrganizationRoles"

    class Rules:
        class GenerateRandomDisplayName(Rule):
            pass

    class Enums:
        class UserInOrganizationRoles(Enum):
            ADMIN = "admin"
            EDITOR = "editor"

    class ApiViews:
        class CreateOrganizationApiView(ApiView):
            pass

        class AddUserToDemoOrganizationApiView(ApiView):
            pass

    class DomainEvents:
        class OrganizationCreated:
            pass

        class UserAddedToOrganization:
            pass

        class UserRemovedFromOrganization:
            pass


g.add_user_to_demo_organization_api_view = (
    Organizations.ApiViews.AddUserToDemoOrganizationApiView()
)
g.add_user_to_organization_action = Organizations.Actions.AddUserToOrganization()
g.create_organization_action = Organizations.Actions.CreateOrganization()
g.create_organization_api_view = Organizations.ApiViews.CreateOrganizationApiView()
g.generate_random_display_name_rule = Organizations.Rules.GenerateRandomDisplayName()


@actor_to_str.method((Organizations.Models.Organization,))
def organization_to_str(organization):
    return f"{organization.name}+:organization"


@actor_to_str.method((Organizations.Models.OrganizationStaffSettings,))
def organization_staff_settings_to_str(organization_staff_settings):
    return (
        f"{organization_staff_settings.organization.name}+:organization-staff-settings"
    )


@actor_to_str.method((Organizations.Models.OrganizationMembership,))
def organization_membership_to_str(organization_membership):
    return (
        f"({organization_membership.organization.name})-"
        + f"({organization_membership.user.email})-"
        + f"({organization_membership.role})+:organization-membership"
    )
