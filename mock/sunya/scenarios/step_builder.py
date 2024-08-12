from sunya.entities import Entity
from mock.sunya.extension.extend import extend
from sunya.extension.memfun import MemFun
from mock.sunya.scenarios.store import NodeContext


def entity_calls(entity, other_entity):
    step_builder = StepBuilder(entity)
    return step_builder.calls(other_entity)


def entity_creates(entity, other_entity):
    step_builder = StepBuilder(entity)
    return step_builder.creates(other_entity)


class StepBuilder:
    def __init__(self, entity):
        self.entity = entity
        self.calls_other_entity = None
        self.creates_other_entity = None
        self.wth_entities = []

    def __enter__(self):
        if self.calls_other_entity:
            verb = "calls"
            other_entity = self.calls_other_entity
        elif self.creates_other_entity:
            verb = "creates"
            other_entity = self.creates_other_entity
        else:
            raise Exception("No verb")

        suffix = []
        if self.wth:
            suffix = ("with", self.wth)

        node = ("The", self.entity, verb, "the", other_entity, *suffix)
        return NodeContext.enter(node)

    def __exit__(self, *args):
        return NodeContext.exit()

    def calls(self, other_entity):
        self.calls_other_entity = other_entity
        return self

    def creates(self, other_entity):
        self.creates_other_entity = other_entity
        return self

    def wth(self, wth):
        self.wth_entities = wth if isinstance(wth, tuple) else (wth,)
        return self


@extend(Entity)
class ExtendEntity:
    calls = MemFun(entity_calls)
    creates = MemFun(entity_creates)
