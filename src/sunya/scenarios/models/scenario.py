import typing as T

from dataclassy import dataclass
from sunya.nodes.models.node import Node
from sunya.scenarios.models.store import store
from sunya.steps.models.step import Step


@dataclass(kw_only=True)
class Scenario:
    name: str
    nodes: T.List[Node] = []
    stack: T.List[Step] = []
    roles: T.List = []
    markdown_fn: str | None = None
    steps: T.List[Step] = []

    @property
    def step(self) -> Step | None:
        if not self.stack:
            return None
        return self.stack[-1]

    def add_step(self, step: Step):
        if not self.step:
            self.steps.append(step)
        else:
            self.step.steps.append(step)


def get_scenario(name: str | None = None) -> Scenario:
    if name is None:
        return store.component.scenario

    for scenario in store.component.scenarios:
        if scenario.name == name:
            return scenario

    raise ScenarioNotFoundError(f"Scenario with name '{name}' not found.")


class ScenarioNotFoundError(Exception):
    pass


class NoNodeError(Exception):
    pass
