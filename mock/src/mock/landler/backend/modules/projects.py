import typing as T

if T.TYPE_CHECKING:
    from mock.landler.backend.modules.plots import Plots

from mock.landler.backend.modules.organizations import Organizations
from kits.python_app.namespace import Enum, Form
from kits.django_app.namespace import Action, ApiView, DjangoModule

from sunya import NowMixin, Entity, FK


class Projects(DjangoModule):
    class Models:
        class Project(NowMixin, Entity):
            name: str
            # Automatically added by Django as related sets
            memberships: T.List["Projects.Models.ProjectMembership"] = []

        class ProjectMembership(Entity):
            role: "Projects.Enums.OrganizationInProjectRoles"
            project: FK["Projects.Models.Project"]
            organization: FK[Organizations.Models.Organization]

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
        class CreateProjectApiView(ApiView):
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
