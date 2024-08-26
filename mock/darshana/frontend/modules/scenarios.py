from default.frontend.namespace import Facet, Route, Component, Action, Ctr, State, Query
from default.stack.namespace import Module
import typing as T
from sunya import (
    actor_to_str,
    EntityWithId,
    G as g,
    str_to_uuid,
    any_dict,
)


class Scenarios(Module):
    class Types:
        class Scenario(EntityWithId):
            name: str
            root_step: "Scenarios.Types.Step"

        class Step(EntityWithId):
            fact: T.Tuple[str]
            parent_step: T.Optional["Scenarios.Types.Step"] = None
            child_steps: T.List["Scenarios.Types.Step"] = []
            field_delta_set_by_actor_key: T.Dict[str, T.Dict[str, T.Any]] = {}

    class Queries:
        class GetScenarios(Query):
            pass

    class States:
        class ScenariosState(State):
            class Containers:
                class ScenariosCtr(Ctr):
                    data: Facet
                    highlight: Facet

        class StepTreeState(State):
            class Containers:
                class StepTreeCtr(Ctr):
                    data: Facet = any_dict(reconstructed_actor=None)

            class Actions:
                set_highlighted_actor = Action(name="setHighlightedActor")

    class Routes:
        class Scenario(Route):
            pass

    class StateProviders:
        class ScenariosStateProvider:
            pass

        class StepTreeStateProvider:
            pass

    class Views:
        class ScenarioListView(Component):
            pass

        class StepTreeView(Component):
            pass

        class StepListView(Component):
            props = dict(
                is_collapsed=False,
            )

        class ScenarioPage(Component):
            root = dict(
                step_tree_view=dict(step_list_views=None),
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
g.step_tree_state = Scenarios.States.StepTreeState()
g.set_highlighted_actor_action = (
    Scenarios.States.StepTreeState.Actions.set_highlighted_actor
)
g.get_scenarios_query = Scenarios.Queries.GetScenarios()

@actor_to_str.method((Scenarios.Types.Scenario,))
def scenario_to_str(scenario):
    return f"{scenario.name}+:scenario"


@actor_to_str.method((Scenarios.Types.Step,))
def step_to_str(step):
    id = str_to_uuid("-".join(step.fact))
    return f"{"-".join(step.fact)}:step"
