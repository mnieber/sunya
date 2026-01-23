from mock.default.stack.namespace import Module, Form
from darshana.backend.modules.scenarios import Scenarios
from mock.default.backend.namespace import Action, ApiView
import typing as T

from sunya import EntityWithId


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

        class UpdateProject(Action):
            class Args:
                update_project_form: Form
                project: "Projects.Models.Project"

        class DeleteProjects(Action):
            class Args:
                project_ids: T.List[str]

        class ImportSpecFiles(Action):
            class Args:
                import_spec_files_form: Form
                project: "Projects.Models.Project"

        class ImportScenarioSpec(Action):
            class Args:
                import_scenario_spec_form: Form
                project: "Projects.Models.Project"

        class ImportModuleSpec(Action):
            class Args:
                import_module_spec_form: Form
                project: "Projects.Models.Project"

    class ApiViews:
        class CreateProject(ApiView):
            pass

        class UpdateProject(ApiView):
            pass

        class DeleteProjects(ApiView):
            pass

        class ImportSpecFiles(ApiView):
            pass

        class GetProject(ApiView):
            pass

        class GetProjectLeads(ApiView):
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
