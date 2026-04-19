import sunya
from sunya import M as m
from sunya import R as r
from sunya import goal, it, the

scenario = sunya.add_scenario(f"mrd4_a_user_creates_a_project")


def run_scenario():
    r.user = m.External.Actors.User
    r.frontend = m.External.Actors.Frontend
    r.set_active_organization_api_view = m.Organizations.ApiViews.SetActiveOrganizationApiView
    r.set_active_organization_action = m.Organizations.Actions.SetActiveOrganization
    r.create_project_api_view = m.Projects.ApiViews.CreateProjectApiView
    r.create_project_action = m.Projects.Actions.CreateProject
    r.add_organization_to_project_action = m.Projects.Actions.AddOrganizationToProject

    with goal().set_the_demo_organization_as_active():
        # Set demo organization as active
        with the(r.frontend).calls(r.set_active_organization_api_view):
            with it().calls(r.set_active_organization_action).to_set_the(r.demo_organization).as_active():
                pass

    with goal().create_a(r.project).in_the(r.demo_organization):
        # Create a project in the demo organization
        with the(r.frontend).calls(r.create_project_api_view):
            with it().calls(r.create_project_action).with_the(r.create_project_form):
                it().creates(r.project).with_default_plot_list()

                # Add organization to project
                with it().calls(r.add_organization_to_project_action).with_the(r.project).and_the(r.demo_organization):
                    it().creates(r.project_membership).with_admin_role()


markdown_node = sunya.add_markdown_node(scenario, "A user creates a project")

markdown_node.markdown = """
A user sets the demo organization as active and then creates a project in that organization. The project is automatically associated with the organization with an admin role.

### Steps

#### It sets the demo organization as active

The frontend calls the set active organization API view.</br>
The API view calls the `SetActiveOrganization` action to set the demo organization as active.</br>

#### It creates the project

The frontend calls the create project API view.</br>
The API view calls the `CreateProject` action with the `create_project_form`.</br>
The action creates the project with a default plot list.</br>
The action calls `AddOrganizationToProject` with the project and demo organization.</br>
The `AddOrganizationToProject` action creates the project membership with admin role.</br>

### Diagram

```mermaid
sequenceDiagram
    actor User
    participant Frontend as Frontend
    participant SetActiveOrganizationApiView as SetActiveOrganizationApiView
    participant SetActiveOrganization as SetActiveOrganization (action)
    participant CreateProjectApiView as CreateProjectApiView
    participant CreateProject as CreateProject (action)
    participant AddOrganizationToProject as AddOrganizationToProject (action)

    Note over Frontend,SetActiveOrganization: Set Active Organization
    User->>Frontend: set active organization
    Frontend->>SetActiveOrganizationApiView: calls
    SetActiveOrganizationApiView->>SetActiveOrganization: set_active_organization(demo_organization)
    SetActiveOrganization->>SetActiveOrganization: set demo_organization as active
    SetActiveOrganization-->>SetActiveOrganizationApiView:

    Note over Frontend,AddOrganizationToProject: Create Project
    User->>Frontend: create project
    Frontend->>CreateProjectApiView: calls
    CreateProjectApiView->>CreateProject: create_project(create_project_form)
    CreateProject->>CreateProject: create project with default plot list
    CreateProject->>AddOrganizationToProject: add_organization_to_project(project, demo_organization, add_organization_to_project_form)
    AddOrganizationToProject->>AddOrganizationToProject: create project membership with admin role
    AddOrganizationToProject-->>CreateProject: project_membership
    CreateProject-->>CreateProjectApiView: project
```
"""
