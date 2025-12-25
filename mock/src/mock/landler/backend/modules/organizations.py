from kits.django_app.impl.namespace import DjangoModule
from kits.python_app.impl.namespace import Enum
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

    class Forms:
        class AddUserToOrganizationForm:
            display_name: str
            member_email: str
            role: "Organizations.Enums.UserInOrganizationRoles"

    class Enums:
        class UserInOrganizationRoles(Enum):
            ADMIN = "admin"
            EDITOR = "editor"

    class DomainEvents:
        class OrganizationCreated:
            pass

        class UserAddedToOrganization:
            pass

        class UserRemovedFromOrganization:
            pass
