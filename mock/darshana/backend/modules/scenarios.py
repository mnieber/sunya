from default.stack.namespace import Module, Form
from default.backend.namespace import Action

from sunya import EntityWithId, actor_to_str, G as g


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
g.update_sce


@actor_to_str.method((Scenarios.Models.Scenario,))
def scenario_to_str(scenario):
    return f"{scenario.name}+:scenario"
