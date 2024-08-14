import typing as T

if T.TYPE_CHECKING:
    from landler.backend.modules.plots import Plots

from landler.backend.modules.organizations import Organizations
from landler.stack.entities import Module, Enum, Form
from blogs.backend.entities import Action, ApiView

from sunya import Entity, actor_to_str, G as g


class Projects(Module):
    class Models:
        class Project(Entity):
            name: str
            memberships: T.List["Projects.Models.ProjectMembership"] = []

        class ProjectMembership(Entity):
            project: "Projects.Models.Project"
            organization: Organizations.Models.Organization
            role: "Projects.Enums.OrganizationInProjectRoles"

    class Actions:
        class CreateProject(Action):
            class Args:
                create_project_form: Form

        class AddOrganizationToProject(Action):
            class Args:
                project: "Projects.Models.Project"
                organization: Organizations.Models.Organization
                role: "Projects.Enums.OrganizationInProjectRoles"

        class AddPlotToProject(Action):
            class Args:
                project: "Projects.Models.Project"
                plot: "Plots.Models.Plot"

    class Api:
        class CreateProject(ApiView):
            pass

    class Enums:
        class OrganizationInProjectRoles(Enum):
            ADMIN = "admin"
            EDITOR = "editor"
            LAND_STEWARD = "land_steward"
            BUYER = "buyer"

    class DomainEvents:
        class ProjectCreated:
            pass

        class OrganizationAddedToProject:
            pass


g.create_project_action = Projects.Actions.CreateProject()
g.create_project_api_view = Projects.Api.CreateProject()
g.add_organization_to_project_action = Projects.Actions.AddOrganizationToProject()
g.add_plot_to_project_action = Projects.Actions.AddPlotToProject()


@actor_to_str.method((Projects.Models.Project,))
def project_to_str(project):
    return f"{project.name}+:project"


@actor_to_str.method((Projects.Models.ProjectMembership,))
def project_membership_to_str(project_membership):
    return (
        f"({project_membership.project.name})-"
        + f"({project_membership.organization.name})-"
        + f"({project_membership.role})+:project-membership"
    )
