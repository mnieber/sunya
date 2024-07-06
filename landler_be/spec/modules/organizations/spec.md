1 Models

1.1 Model: Organization

id: UUID
name: str
memberships: list[OrganizationMembership]

1.2 Model: OrganizationMembership

organization: Organization
user: User
role: UserInOrganizationRoles

2 Enums

2.1 Enum: UserInOrganizationRoles

Items:
admin
editor

3 Actions

3.1 Action: create_organization

Arguments:
create_organization_form: Form

3.2 Action: add_user_to_organization

Arguments:
organization: Organization
user: User
role: UserInOrganizationRoles

4 Api views

4.1 Api view: CreateOrganizationApiView


