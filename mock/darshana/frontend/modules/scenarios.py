from default.frontend.namespace import (
    Route,
    Component,
)
from default.stack.namespace import Module
from sunya import (
    actor_to_str,
    EntityWithId,
    G as g,
)
from darshana.frontend.modules.steps import Steps


class Scenarios(Module):
    class Types:
        class Scenario(EntityWithId):
            name: str
            root_step: "Steps.Types.Step"

    class Routes:
        class Scenario(Route):
            pass

    class Views:
        class ScenarioListView(Component):
            pass

        class ScenarioPage(Component):
            root = dict(
                step_tree_view=dict(step_list_views=None),
                actor_view=None,
            )

    class Effects:
        class SelectScenarioEffect:
            pass


g.scenario_route = Scenarios.Routes.Scenario()
g.scenario_list_view = Scenarios.Views.ScenarioListView()


@actor_to_str.method((Scenarios.Types.Scenario,))
def scenario_to_str(scenario):
    return f"{scenario.name}+:scenario"
