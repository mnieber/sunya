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

class Steps(Module):
    class Types:
        class FactBit(Entity):
            type: str = "string | role | actor"
            value: str

        class Step(EntityWithId):
            fact: T.Tuple["Steps.Types.FactBit"]
            parent_step: T.Optional["Steps.Types.Step"] = None
            child_steps: T.List["Steps.Types.Step"] = []
            fieldDeltaSetByActorKey: T.Dict[str, T.Dict[str, T.Any]] = {}

    class States:
        class StepTreeState(State):
            class Containers:
                class StepTreeCtr(Ctr):
                    data: Facet = any_dict(reconstructed_actor=None)

            class Actions:
                set_highlighted_actor = Action(name="setHighlightedActor")

    class StateProviders:
        class StepTreeStateProvider:
            pass

    class Views:
        class StepTreeView(Component):
            pass

        class StepListView(Component):
            props = dict(
                step="StepT",
            )
            local_state= dict(
                is_collapsed=False,
            )

    class Effects:
        class SelectStepEffect:
            pass


g.step_tree_view = Steps.Views.StepTreeView()
g.step_list_view = Steps.Views.StepListView()
g.step_tree_state = Steps.States.StepTreeState()
g.set_highlighted_actor_action = (
    Steps.States.StepTreeState.Actions.set_highlighted_actor
)


@actor_to_str.method((Steps.Types.Step,))
def step_to_str(step):
    id = str_to_uuid("-".join(step.fact))
    return f"{"-".join(step.fact)}:step"
