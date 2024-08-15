from darshana.frontend.entities import Mutation, Query, Facet, Route
from darshana.stack.namespace import Module, Form
import typing as T
from sunya import actor_to_str, G as g
from .scenarios import Scenarios


class Projects(Module):
    class Types:
        class Project(T.TypedDict):
            name: str
            scenarios: T.List["Scenarios.Types.Scenario"]

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
        class ProjectsPage:
            class Root:
                __ProjectList: None
                __CreateProjectForm: None

        class ProjectPage:
            class Root:
                __ScenarioList: None

        class ProjectListView:
            pass

        class CreateProjectFormView:
            pass

    class Components:
        class ImportFilesButton:
            pass

        class CreateProjectButton:
            pass

    class Effects:
        class SelectProjectEffect:
            pass


g.projects_route = Projects.Routes.Projects()
g.project_route = Projects.Routes.Project()
g.create_project_mutation = Projects.Mutations.CreateProject()


@actor_to_str.method((Projects.Types.Project,))
def project_to_str(project):
    return f"{project.name}+:project"
