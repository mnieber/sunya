from sunya.steps.models.step import Step
from sunya.steps.models.rel import Rel
from sunya.steps.rules.self import Self


def signal(from_actor: any, to_actor: any, dashed=False):
    from sunya.scenarios.models.scenario import get_scenario

    if isinstance(to_actor, Self):
        to_actor = from_actor

    goal = get_scenario().get_node().get_goal()
    step = Step(rel=Rel(fact_bits=(from_actor, to_actor)))
    goal.steps.append(step)

    connector = "-->>" if dashed else "->>"
    return f"{from_actor.name} {connector} {to_actor.name}<remove_whitespace/>"
