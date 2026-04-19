import sunya
from sunya import M as m
from sunya import R as r
from sunya import goal, it, the

scenario = sunya.add_scenario(f"mrd2_a_user_creates_an_org_and_invites_a_user")


def run_scenario():
    r.user = m.External.Actors.User
    r.frontend = m.External.Actors.Frontend
    r.create_organization_api_view = m.Organizations.ApiViews.CreateOrganizationApiView
    r.create_organization_action = m.Organizations.Actions.CreateOrganization
    r.add_user_to_organization_action = m.Organizations.Actions.AddUserToOrganization
    r.set_active_organization_api_view = m.Organizations.ApiViews.SetActiveOrganizationApiView
    r.set_active_organization_action = m.Organizations.Actions.SetActiveOrganization

    with goal().create_an(r.organization).for_the(r.user):
        # Create organization
        with the(r.frontend).calls(r.create_organization_api_view):
            with it().calls(r.create_organization_action).with_the(r.create_organization_form):
                it().creates(r.organization)

                # Add user to organization as admin
                with it().calls(r.add_user_to_organization_action).with_the(r.organization).and_the(r.user):
                    it().creates(r.organization_membership)

    with goal().set(r.organization).as_the_active_organization():
        # Set active organization
        with the(r.frontend).calls(r.set_active_organization_api_view):
            with it().calls(r.set_active_organization_action).with_the(r.organization):
                it().sets(r.organization).as_the_active_organization_in_the_user_session()


markdown_node = sunya.add_markdown_node(scenario, "A user creates an org and invites a user")

markdown_node.markdown = """
A user creates an organization and is automatically added as an admin. Then the user sets the organization as their active organization.

### Steps

#### It creates the organization

The frontend calls the create organization API view.</br>
The API view calls the `CreateOrganization` action with the `create_organization_form`.</br>
The action creates the organization.</br>
The action calls `AddUserToOrganization` with the organization, user, and admin role.</br>
The `AddUserToOrganization` action creates the organization membership.</br>

#### It sets the active organization

The frontend calls the set active organization API view.</br>
The API view calls the `SetActiveOrganization` action with the organization.</br>
The action sets the organization as the active organization in the user session.</br>

### Diagram

```mermaid
sequenceDiagram
    actor User
    participant Frontend as Frontend
    participant CreateOrganizationApiView as CreateOrganizationApiView
    participant CreateOrganization as CreateOrganization (action)
    participant AddUserToOrganization as AddUserToOrganization (action)
    participant SetActiveOrganizationApiView as SetActiveOrganizationApiView
    participant SetActiveOrganization as SetActiveOrganization (action)

    Note over Frontend,AddUserToOrganization: Create Organization
    User->>Frontend: create organization
    Frontend->>CreateOrganizationApiView: calls
    CreateOrganizationApiView->>CreateOrganization: create_organization(create_organization_form)
    CreateOrganization->>CreateOrganization: create organization
    CreateOrganization->>AddUserToOrganization: add_user_to_organization(organization, user, admin_role)
    AddUserToOrganization->>AddUserToOrganization: create organization membership
    AddUserToOrganization-->>CreateOrganization: organization_membership
    CreateOrganization-->>CreateOrganizationApiView: organization

    Note over Frontend,SetActiveOrganization: Set Active Organization
    User->>Frontend: set active organization
    Frontend->>SetActiveOrganizationApiView: calls
    SetActiveOrganizationApiView->>SetActiveOrganization: set_active_organization(organization)
    SetActiveOrganization->>SetActiveOrganization: set organization as active in user session
    SetActiveOrganization-->>SetActiveOrganizationApiView:
```
"""
