from sunya.scenarios.models.goal import Goal
from sunya.scenarios.models.scenario import get_scenario
from sunya.steps.models.rel import Rel
from sunya.steps.rules.rel_to_string import rel_to_string


def goal(rel: Rel):
    scenario = get_scenario()
    node = scenario.get_node()
    node.goals.append(Goal(rel=rel))

    return rel_to_string(rel)
