import typing as T
from sunya.entities.utils.actor_to_str import actor_to_str  # noqa


def the(entity):
    from sunya.scenarios.actions.step_builder import StepBuilder

    step_builder = StepBuilder(fact_bits=(The(entity),))
    return T.cast(T.Any, step_builder)


class The:
    def __init__(self, entity):
        self.entity = entity

    def __repr__(self):
        return f"The({actor_to_str(self.entity)})"


class CallsThe(The):
    def __repr__(self):
        return f"CallsThe({actor_to_str(self.entity)})"
