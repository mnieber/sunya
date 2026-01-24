from sunya.steps.models.step import Step
from sunya.steps.models.rel import Rel


class Message:
    def __init__(self, from_actor, to_actor, dashed=False):
        self.from_actor = from_actor
        self.to_actor = to_actor
        self.dashed = dashed

    def __sub__(self, rel: Rel):
        from sunya.scenarios.models.scenario import get_scenario

        rel.fact_bits = (self.from_actor, *rel.fact_bits, self.to_actor)
        step = Step(rel=rel)
        goal = get_scenario().get_node().get_goal()
        goal.steps.append(step)

        connector = "-->>" if self.dashed else "->>"
        return f"{self.from_actor.name} {connector} {self.to_actor.name}: {rel}"

    def __str__(self):
        connector = "-->>" if self.dashed else "->>"
        return f"{self.from_actor.name} {connector} {self.to_actor.name}"
