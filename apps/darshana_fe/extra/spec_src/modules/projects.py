from mock.default.frontend.namespace import (
    Facet,
    Action,
    Component,
    Mutation,
    Query,
    Facet,
    Route,
    Component,
)
from mock.default.stack.namespace import Module, Form
import typing as T
from sunya import EntityWithId, any_dict
from .scenarios import Scenarios


class Projects(Module):
    class Types:
        class ProjectLead(EntityWithId):
            name: str
            description: str = ""

        class Project(EntityWithId):
            name: str
            description: str = ""
            scenarios: T.List["Scenarios.Types.Scenario"] = []

    class Mutations:
        class CreateProject(Mutation):
            class Args:
                createProjectForm: Form

        class UpdateProject(Mutation):
            class Args:
                updateProjectForm: Form

        class DeleteProjects(Mutation):
            class Args:
                project_ids: T.List[str]

        class ImportSpecFiles(Mutation):
            class Args:
                project: "Projects.Types.Project"
                files: T.List[T.Any]

    class Queries:
        class GetProjectLeads(Query):
            pass

        class GetProject(Query):
            class Args:
                projectId: str

    class States:
        class ProjectLeadsState:
            class Containers:
                class ProjectLeadsCtr:
                    data: Facet
                    highlight: Facet
                    deletion: Facet = any_dict()
                    edit: Facet = any_dict()

        class ProjectState:
            class Containers:
                class ProjectCtr:
                    data: Facet

                class ScenariosCtr:
                    data: Facet
                    highlight: Facet

                class ActionsCtr:
                    upload_spec_files = Action(name="importSpecFiles")

    class Routes:
        class Projects(Route):
            pass

        class Project(Route):
            pass

    class StateProviders:
        class ProjectLeadsStateProvider:
            pass

        class ProjectStateProvider:
            pass

    class Views:
        class ProjectsPage(Component):
            root = dict(
                #
                project_list=None,
            )

        class ProjectPage(Component):
            root = dict(
                #
                scenario_list_view=None
            )

        class ProjectListView(Component):
            pass

        class ProjectLeadFormView(Component):
            pass

        class ImportSpecFilesFormView(Component):
            pass

    class Components:
        class ImportSpecFilesButton(Component):
            pass

        class CreateProjectButton(Component):
            pass

        class DeleteProjectButton(Component):
            pass

    class Effects:
        class SelectProjectEffect(Component):
            pass
