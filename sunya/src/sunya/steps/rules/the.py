
from sunya.scenarios.models.scenario import get_scenario
from sunya.steps.models.step import Step


def the(entity):
    from sunya.steps.models.rel import Rel

    rel = Rel(fact_bits=(The(entity),))
    step = Step(rel=rel)
    get_scenario().add_step(step)
    return step


class The:
    def __init__(self, entity):
        self.entity = entity
