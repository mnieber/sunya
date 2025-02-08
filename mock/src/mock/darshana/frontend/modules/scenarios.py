from mock.default.frontend.namespace import (
    Route,
    Component,
)
from mock.default.stack.namespace import Module
from sunya import (
    EntityWithId,
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
