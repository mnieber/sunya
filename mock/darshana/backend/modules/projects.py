from default.stack.namespace import Module, Form, Enum
from default.backend.namespace import Action, ApiView
import typing as T

from sunya import EntityWithId, actor_to_str, G as g


class Projects(Module):
    class Models:
        class Project(EntityWithId):
            name: str
            description: T.Optional[str]
            scenarios: T.List["Scenarios.Models.Scenario"] = []

    class Actions:
        class CreateProject(Action):
            class Args:
                create_project_form: Form

        class SaveProject(Action):
            class Args:
                save_project_form: Form
                project: "Projects.Models.Project"

        class DeleteProjects(Action):
            class Args:
                project_ids: T.List[str]

        class UploadSpecFiles(Action):
            class Args:
                project: "Projects.Models.Project"
                files: T.List[T.Any]

    class ApiViews:
        class CreateProject(ApiView):
            pass

        class SaveProject(ApiView):
            pass

        class DeleteProjects(ApiView):
            pass

        class UploadSpecFiles(ApiView):
            pass

        class GetProject(ApiView):
            pass

        class GetProjects(ApiView):
            pass

    class DomainEvents:
        class ProjectCreated:
            pass

        class ProjectUpdated:
            pass

        class ProjectDeleted:
            pass

        class SpecFilesUploaded:
            pass


g.create_project_action = Projects.Actions.CreateProject()
g.save_project_action = Projects.Actions.SaveProject()
g.delete_projects_action = Projects.Actions.DeleteProjects()
g.upload_spec_files_action = Projects.Actions.UploadSpecFiles()
g.create_project_api_view = Projects.ApiViews.CreateProject()
g.save_project_api_view = Projects.ApiViews.SaveProject()
g.delete_projects_api_view = Projects.ApiViews.DeleteProjects()
g.upload_spec_files_api_view = Projects.ApiViews.UploadSpecFiles()
g.get_project_api_view = Projects.ApiViews.GetProject()
g.get_projects_api_view = Projects.ApiViews.GetProjects()


@actor_to_str.method((Projects.Models.Project,))
def project_to_str(project):
    return f"{project.name}+:project"
