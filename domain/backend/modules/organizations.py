import typing as T
from uuid import UUID

from dataclassy import Internal
from mock.backend.modules.users import Users
from mock.datatypes import Action, ApiView, Form, Module
from sunya import Entity, actor_to_str


class Organizations(Module):
    class Models:
        class Organization(Entity):
            """A Django model that contains a organization."""

            id: UUID
            name: str
            memberships: Internal[
                T.List["Organizations.Models.OrganizationMembership"]
            ] = []

        class OrganizationMembership(Entity):
            """A Django model that contains a membership of an organization."""

            organization: "Organizations.Models.Organization"
            user: Users.Models.User
            role: Users.Enums.UserRoles

    class Actions:
        class CreateOrganization(Action):
            class Args:
                create_organization_form: Form

        class AddUserToOrganization(Action):
            class Args:
                organization: "Organizations.Models.Organization"
                user: Users.Models.User
                role: Users.Enums.UserRoles

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
