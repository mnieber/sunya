from mock.default.stack.namespace import Module, Form
from mock.default.backend.namespace import Action
from darshana.backend.modules.steps import Steps
from sunya import EntityWithId
import typing as T

if T.TYPE_CHECKING:
    from darshana.backend.modules.projects import Projects


class Scenarios(Module):
    class Models:
        class Scenario(EntityWithId):
            name: str
            project: "Projects.Models.Project"
            root_step: "Steps.Models.Step"

    class Actions:
        class CreateScenario(Action):
            class Args:
                create_scenario_form: Form
                project: "Projects.Models.Project"

    class DomainEvents:
        pass
