from default.frontend.entities import Mutation, Query, Facet, Route, Component
from default.stack.namespace import Module, Form
import typing as T
from sunya import actor_to_str, EntityWithId, G as g
from .scenarios import Scenarios


class Projects(Module):
    class Types:
        class ProjectLead(EntityWithId):
            name: str

        class Project(EntityWithId):
            name: str
            scenarios: T.List["Scenarios.Types.Scenario"] = []

    class Mutations:
        class CreateProject(Mutation):
            class Args:
                createProjectForm: Form

        class UploadSpecFiles(Mutation):
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

        class ProjectState:
            class Containers:
                class ProjectCtr:
                    data: Facet

                class ScenariosCtr:
                    data: Facet
                    highlight: Facet

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

        class CreateProjectFormView(Component):
            pass

        class UploadSpecFilesFormView(Component):
            pass

    class Components:
        class UploadSpecFilesButton(Component):
            pass

        class CreateProjectButton(Component):
            pass

    class Effects:
        class SelectProjectEffect(Component):
            pass


g.create_project_button = Projects.Components.CreateProjectButton()
g.create_project_form_view = Projects.Views.CreateProjectFormView()
g.create_project_mutation = Projects.Mutations.CreateProject()
g.get_project_leads_query = Projects.Queries.GetProjectLeads()
g.get_project_query = Projects.Queries.GetProject()
g.project_page = Projects.Views.ProjectPage()
g.project_route = Projects.Routes.Project()
g.projects_route = Projects.Routes.Projects()
g.upload_spec_files_form_view = Projects.Views.UploadSpecFilesFormView()
g.upload_spec_files_button = Projects.Components.UploadSpecFilesButton()
g.upload_spec_files_mutation = Projects.Mutations.UploadSpecFiles()


@actor_to_str.method((Projects.Types.Project,))
def project_to_str(project):
    return f"{project.name}+:project"
