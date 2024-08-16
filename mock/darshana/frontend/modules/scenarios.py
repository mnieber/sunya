from darshana.frontend.entities import Facet, Route
from darshana.stack.namespace import Module
import typing as T
from sunya import EntityWithId, G as g


class Scenarios(Module):
    class Types:
        class Scenario(EntityWithId):
            name: str
            root_step: "Scenarios.Types.Step"

        class Step(EntityWithId):
            fact: T.List[str]
            child_steps: T.List["Scenarios.Types.Step"]

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
        class ScenarioListView:
            pass

        class ScenarioPage:
            class Root:
                class StepListView:
                    pass

                class StepView:
                    None

                class ActorView:
                    pass

    class Effects:
        class SelectScenarioEffect:
            pass

        class SelectStepEffect:
            pass


g.scenario_route = Scenarios.Routes.Scenario()
