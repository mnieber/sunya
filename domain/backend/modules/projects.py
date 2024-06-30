import typing as T

from dataclassy import Internal

if T.TYPE_CHECKING:
    from mock.app import Plots

from mock.backend.modules.organizations import Organizations
from mock.datatypes import Action, ApiView, Enum, Form, Module
from sunya import Entity, actor_to_str, get_actor_key


class Projects(Module):
    class Models:
        class Project(Entity):
            """A Django model that contains a project."""

            name: str
            memberships: Internal[T.List["Projects.Models.ProjectMembership"]] = []

        class ProjectMembership(Entity):
            """A Django model that contains a membership of a project."""

            project: "Projects.Models.Project"
            organization: Organizations.Models.Organization
            role: "Projects.Enums.ProjectRoles"

    class Actions:
        class CreateProject(Action):
            class Args:
                create_project_form: Form

        class AddOrganizationToProject(Action):
            class Args:
                project: "Projects.Models.Project"
                organization: Organizations.Models.Organization
                role: "Projects.Enums.ProjectRoles"

        class AddPlotToProject(Action):
            class Args:
                project: "Projects.Models.Project"
                plot: "Plots.Models.Plot"

    class Api:
        class CreateProject(ApiView):
            pass

    class Enums:
        class ProjectRoles(Enum):
            ADMIN = "admin"
            EDITOR = "editor"
            LAND_STEWARD = "land_steward"
            BUYER = "buyer"

    class DomainEvents:
        class ProjectCreated:
            pass

        class OrganizationAddedToProject:
            pass


create_project_action = Projects.Actions.CreateProject()
create_project_api_view = Projects.Api.CreateProject()
add_organization_to_project_action = Projects.Actions.AddOrganizationToProject()
add_plot_to_project_action = Projects.Actions.AddPlotToProject()


@actor_to_str.method((Projects.Models.Project,))
def project_to_str(project):
    return f"{project.name}+:project"


@get_actor_key.method((Projects.Models.Project,))
def get_project_key(project):
    return project.name
