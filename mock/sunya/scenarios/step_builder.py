from sunya.scenarios.node import Node
from sunya.extension.extend import extend
from sunya.extension.memfun import MemFun
from sunya.scenarios.store import NodeContext
import typing as T


def entity_calls(step_builder, other_entity):
    step_builder.fact = (*step_builder.fact, "calls the", other_entity)
    return step_builder


def entity_creates(step_builder, other_entity):
    step_builder.fact = (*step_builder.fact, "creates the", other_entity)
    return step_builder


def entity_visits(step_builder, other_entity):
    step_builder.fact = (*step_builder.fact, "visits the", other_entity)
    return step_builder


def entity_submits_a_form(step_builder):
    step_builder.fact = (*step_builder.fact, "submits a form")
    return step_builder


class StepBuilder:
    def __init__(self, entity, fact=None):
        self.entity = entity
        self.fact = fact or tuple()

    def __enter__(self):
        return NodeContext.enter(Node(fact=self.fact))

    def __exit__(self, *args):
        return NodeContext.exit()

    def with_the(self, with_the):
        with_the_entities = with_the if isinstance(with_the, tuple) else (with_the,)
        self.fact = (*self.fact, "with", *with_the_entities)
        return self


@extend(StepBuilder)
class ExtendStepBuilder:
    calls_the = MemFun(entity_calls)
    creates_the = MemFun(entity_creates)
    visits_the = MemFun(entity_visits)
    submits_a_form = MemFun(entity_submits_a_form)


def the(entity):
    step_builder = StepBuilder(entity, fact=("The", entity))
    return T.cast(T.Any, step_builder)
