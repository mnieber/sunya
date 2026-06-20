import sunya
from sunya import M as m
from sunya import R as r
from sunya import goal, it, the

scenario = sunya.add_scenario(f"MRD3: A user joins the demo org")


def run_scenario():
    r.user = m.External.Actors.User
    r.frontend = m.External.Actors.Frontend
    r.add_user_to_demo_organization_api_view = m.Organizations.ApiViews.AddUserToDemoOrganizationApiView
    r.add_user_to_demo_organization_action = m.Organizations.Actions.AddUserToDemoOrganization
    r.create_organization_action = m.Organizations.Actions.CreateOrganization
    r.create_random_display_name_rule = m.Organizations.Rules.CreateRandomDisplayName
    r.add_user_to_organization_action = m.Organizations.Actions.AddUserToOrganization

    with goal().add_the(r.user).to_the(r.demo_organization):
        # Add user to demo organization
        with the(r.frontend).calls(r.add_user_to_demo_organization_api_view):
            with it().calls(r.add_user_to_demo_organization_action).with_the(r.current_user):
                # Find or create demo organization
                with it().finds_the(r.demo_organization):
                    pass  # if not found, will create

                with it().calls(r.create_organization_action).if_demo_org_not_found():
                    it().creates(r.demo_organization).with_name("demo")

                # Create random display name
                with it().calls(r.create_random_display_name_rule):
                    it().generates(r.display_name)

                # Add user to organization
                with it().calls(r.add_user_to_organization_action).with_the(r.demo_organization).and_the(r.current_user):
                    it().creates(r.demo_organization_membership).with_fake_email()


markdown_node = sunya.add_markdown_node(scenario, "A user joins the demo org")

markdown_node.markdown = """
A user joins the demo organization. The system finds or creates the demo organization, generates a random display name for the user, and adds the user to the organization with a fake email address.

### Steps

#### It finds or creates the demo organization

The frontend calls the add user to demo organization API view.</br>
The API view calls the `AddUserToDemoOrganization` action with the current user.</br>
The action finds the demo organization, or creates it if it doesn't exist.</br>

#### It adds the user to the demo organization

The action calls the `CreateRandomDisplayName` rule to generate a display name.</br>
The action calls `AddUserToOrganization` with the demo organization and current user.</br>
The `AddUserToOrganization` action creates the demo organization membership with a fake email address.</br>

### Diagram

```mermaid
sequenceDiagram
    actor User
    participant Frontend as Frontend
    participant AddUserToDemoOrganizationApiView as AddUserToDemoOrganizationApiView
    participant AddUserToDemoOrganization as AddUserToDemoOrganization (action)
    participant CreateOrganization as CreateOrganization (action)
    participant CreateRandomDisplayName as CreateRandomDisplayName (rule)
    participant AddUserToOrganization as AddUserToOrganization (action)

    Note over Frontend,AddUserToOrganization: Add user to demo org
    User->>Frontend: join demo organization
    Frontend->>AddUserToDemoOrganizationApiView: calls(current_user)
    AddUserToDemoOrganizationApiView->>AddUserToDemoOrganization: add_user_to_demo_organization(current_user)
    AddUserToDemoOrganization->>AddUserToDemoOrganization: find demo organization

    alt organization not found
        AddUserToDemoOrganization->>CreateOrganization: create_organization(create_organization_form)
        CreateOrganization->>CreateOrganization: create demo organization
        CreateOrganization-->>AddUserToDemoOrganization: demo_organization
    end

    AddUserToDemoOrganization->>CreateRandomDisplayName: create_random_display_name()
    CreateRandomDisplayName-->>AddUserToDemoOrganization: display_name
    AddUserToDemoOrganization->>AddUserToOrganization: add_user_to_organization(demo_organization, current_user, add_user_to_organization_form)
    AddUserToOrganization->>AddUserToOrganization: create demo organization membership
    AddUserToOrganization-->>AddUserToDemoOrganization: demo_organization_membership
```
"""
