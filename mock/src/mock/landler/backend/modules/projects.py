import typing as T

if T.TYPE_CHECKING:
    from mock.landler.backend.modules.plots import Plots

from mock.landler.backend.modules.organizations import Organizations
from kits.python_app.impl.namespace import Enum
from kits.django_app.impl.namespace import Action, DjangoModule

from sunya import NowMixin, Entity, FK, RelatedSet


class Projects(DjangoModule):
    class Models:
        class Project(NowMixin, Entity):
            name: str
            memberships: RelatedSet["Projects.Models.ProjectMembership"] = []

        class ProjectMembership(Entity):
            role: "Projects.Enums.OrganizationInProjectRoles"
            project: FK["Projects.Models.Project"]
            organization: FK[Organizations.Models.Organization]

    class Forms:
        class AddOrganizationToProjectForm:
            role: "Projects.Enums.OrganizationInProjectRoles"

    class Actions:
        class AddPlotToProject(Action):
            class Args:
                project: "Projects.Models.Project"
                plot: "Plots.Models.Plot"
                plot_list_name: T.Optional[str] = None

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
