from sunya.scenarios.models.scenario import get_scenario
from sunya.steps.models.rel import Rel
from sunya.steps.models.step import Step


class It:
    def __repr__(self):
        return "It"


def it():

    rel = Rel(fact_bits=(It(),))
    step = Step(rel=rel)
    get_scenario().add_step(step)
    return step
