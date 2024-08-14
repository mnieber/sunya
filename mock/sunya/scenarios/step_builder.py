from sunya.scenarios.store import NodeContext
import typing as T
from sunya.scenarios.store import add_node
from sunya.scenarios.store import create_step


class StepBuilder:
    def __init__(self, entity, fact=None):
        self.entity = entity
        self.fact = fact or tuple()

    def __getattr__(self, name):
        def relates_to(other_entity=None):
            other = tuple() if other_entity is None else (other_entity,)
            self.fact = (*self.fact, name.replace("_", " "), *other)
            return self

        return relates_to

    def __enter__(self):
        node = add_node(create_step(self.fact))
        return NodeContext.enter(node)

    def __exit__(self, *args):
        return NodeContext.exit()

    def with_the(self, with_the):
        with_the_entities = with_the if isinstance(with_the, tuple) else (with_the,)
        self.fact = (*self.fact, "with", *with_the_entities)
        return self


def the(entity):
    step_builder = StepBuilder(entity, fact=("The", entity))
    return T.cast(T.Any, step_builder)
