# Module: organizations

## Organizations

```python
class Organizations(DjangoModule):
    class Models:
        class Organization(Entity):
            name: str
            memberships: RelatedSet['Organizations.Models.OrganizationMembership'] = []
            staff_settings: FK['Organizations.Models.OrganizationStaffSettings'] = any_dict()

        class OrganizationMembership(Entity):
            role: 'Organizations.Enums.UserInOrganizationRoles'
            display_name: str
            member_email: str
            organization: FK['Organizations.Models.Organization']
            user: FK[Users.Models.User]

        class OrganizationStaffSettings(Entity):
            is_managed_by_tlg: bool
            is_demo_org: bool
            organization: FK['Organizations.Models.Organization']

    class Forms:
        class AddUserToOrganizationForm:
            display_name: str
            member_email: str
            role: 'Organizations.Enums.UserInOrganizationRoles'

    class Enums:
        class UserInOrganizationRoles(Enum):
            ADMIN: Any = 'admin'
            EDITOR: Any = 'editor'

    class DomainEvents:
        class OrganizationCreated:
            pass

        class UserAddedToOrganization:
            pass

        class UserRemovedFromOrganization:
            pass
```

