from sunya.scenarios.models.goal import Goal
from sunya.scenarios.models.scenario import get_scenario
from sunya.steps.models.rel import Rel


def goal(fact_bits):
    rel = Rel(*fact_bits)
    goal = Goal(rel=rel)
    get_scenario().add_step(goal)
    return goal
