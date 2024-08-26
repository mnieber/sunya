from default.frontend.entities import Mutation, Query, Facet, Route, Component
from default.stack.namespace import Module, Form
import typing as T
from sunya import actor_to_str, EntityWithId, G as g
from .scenarios import Scenarios


class Projects(Module):
    class Types:
        class Project(EntityWithId):
            name: str
            scenarios: T.List["Scenarios.Types.Scenario"] = []

    class Mutations:
        class CreateProject(Mutation):
            class Args:
                createProjectForm: Form

        class ImportSpecFiles(Mutation):
            class Args:
                project: "Projects.Types.Project"
                files: T.List[T.Any]

        class DeleteUploadedFile(Mutation):
            class Args:
                filename: str

    class Queries:
        class GetProjects(Query):
            pass

        class GetProject(Query):
            class Args:
                projectId: str

    class States:
        class ProjectsState:
            class Containers:
                class ProjectsCtr:
                    data: Facet
                    highlight: Facet

    class Routes:
        class Projects(Route):
            pass

        class Project(Route):
            pass

    class StateProviders:
        class ProjectsStateProvider:
            pass

    class Views:
        class ProjectsPage(Component):
            class Root:
                root = dict(
                    #
                    project_list=None,
                    create_project_form=None,
                )

        class ProjectPage(Component):
            root = dict(
                #
                scenario_list_view=None
            )

        class ProjectListView(Component):
            pass

        class CreateProjectFormView(Component):
            pass

    class Components:
        class ImportFilesButton(Component):
            pass

        class CreateProjectButton(Component):
            pass

    class Effects:
        class SelectProjectEffect(Component):
            pass


g.import_files_button = Projects.Components.ImportFilesButton()
g.create_project_button = Projects.Components.CreateProjectButton()
g.projects_route = Projects.Routes.Projects()
g.project_route = Projects.Routes.Project()
g.create_project_mutation = Projects.Mutations.CreateProject()
g.project_page = Projects.Views.ProjectPage()
g.get_project_query = Projects.Queries.GetProject()


@actor_to_str.method((Projects.Types.Project,))
def project_to_str(project):
    return f"{project.name}+:project"
