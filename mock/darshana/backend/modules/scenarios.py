from default.stack.namespace import Module, Form
from default.backend.namespace import Action
from darshana.backend.modules.steps import Steps
from sunya import EntityWithId, actor_to_str, G as g
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


g.create_scenario_action = Scenarios.Actions.CreateScenario()


@actor_to_str.method((Scenarios.Models.Scenario,))
def scenario_to_str(scenario):
    return f"{scenario.name}+:scenario"
