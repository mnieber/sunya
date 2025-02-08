from mock.django_app.namespace import Action, ApiView, Rule, DjangoModule
from mock.python_app.namespace import Enum, Form
from mock.landler.backend.modules.users import Users
from sunya import Entity, RelatedSet, FK
from sunya.utils.any_dict import any_dict


class Organizations(DjangoModule):
    class Models:
        class Organization(Entity):
            name: str
            # Automatically added by Django as related sets
            memberships: RelatedSet["Organizations.Models.OrganizationMembership"] = []
            staff_settings: FK["Organizations.Models.OrganizationStaffSettings"] = (
                any_dict()
            )

        class OrganizationMembership(Entity):
            role: "Organizations.Enums.UserInOrganizationRoles"
            display_name: str
            member_email: str
            organization: FK["Organizations.Models.Organization"]
            user: FK[Users.Models.User]

        class OrganizationStaffSettings(Entity):
            is_managed_by_tlg: bool
            is_demo_org: bool
            organization: FK["Organizations.Models.Organization"]

    class Actions:
        class CreateOrganization(Action):
            class Args:
                create_organization_form: Form

        class AddUserToDemoOrganization(Action):
            class Args:
                user: Users.Models.User

        class AddUserToOrganization(Action):
            class Args:
                organization: "Organizations.Models.Organization"
                user: Users.Models.User
                role: "Organizations.Enums.UserInOrganizationRoles"

        class SetActiveOrganization(Action):
            class Args:
                organization: "Organizations.Models.Organization"
                user: Users.Models.User

    class Rules:
        class GenerateRandomDisplayName(Rule):
            pass

    class Enums:
        class UserInOrganizationRoles(Enum):
            ADMIN = "admin"
            EDITOR = "editor"

    class Api:
        class CreateOrganizationApiView(ApiView):
            pass

        class AddUserToDemoOrganizationApiView(ApiView):
            pass

        class SetActiveOrganizationApiView(ApiView):
            pass

    class DomainEvents:
        class OrganizationCreated:
            pass

        class UserAddedToOrganization:
            pass

        class UserRemovedFromOrganization:
            pass
