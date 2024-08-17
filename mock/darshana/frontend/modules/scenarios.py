from darshana.frontend.entities import Facet, Route, Component
from darshana.stack.namespace import Module
import typing as T
from sunya import actor_to_str, EntityWithId, G as g, str_to_uuid


class Scenarios(Module):
    class Types:
        class Scenario(EntityWithId):
            name: str
            root_step: "Scenarios.Types.Step"

        class Step(EntityWithId):
            fact: T.Tuple[str] = tuple()
            child_steps: T.List["Scenarios.Types.Step"] = []

    class States:
        class ScenariosState:
            class Containers:
                class ScenariosCtr:
                    data: Facet
                    highlight: Facet

        class StepListState:
            class Containers:
                class StepListCtr:
                    data: Facet
                    highlight: Facet

    class Routes:
        class Scenario(Route):
            pass

    class StateProviders:
        class ScenariosStateProvider:
            pass

        class StepListStateProvider:
            pass

    class Views:
        class ScenarioListView(Component):
            pass

        class StepTreeView(Component):
            pass

        class StepListView(Component):
            pass

        class StepView(Component):
            pass

        class ScenarioPage(Component):
            root = dict(
                step_tree_view=dict(step_list_views=None),
                step_view=None,
                actor_view=None,
            )

    class Effects:
        class SelectScenarioEffect:
            pass

        class SelectStepEffect:
            pass


g.scenario_route = Scenarios.Routes.Scenario()
g.scenario_list_view = Scenarios.Views.ScenarioListView()
g.step_tree_view = Scenarios.Views.StepTreeView()
g.step_list_view = Scenarios.Views.StepListView()
g.step_view = Scenarios.Views.StepView()


@actor_to_str.method((Scenarios.Types.Scenario,))
def scenario_to_str(scenario):
    return f"{scenario.name}:scenario"


@actor_to_str.method((Scenarios.Types.Step,))
def step_to_str(step):
    id = str_to_uuid("-".join(step.fact))
    return f"{id}:step"
