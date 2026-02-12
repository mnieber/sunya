import typing as T
from sunya.scenarios.models.store import store
from sunya.nodes.models.node import Node

from dataclassy import dataclass


@dataclass(kw_only=True)
class Scenario:
    name: str
    nodes: T.List[Node] = []
    roles: T.List = []

    def get_node(self) -> Node:
        if not self.nodes:
            raise NoNodeError("No nodes in the current scenario.")
        return self.nodes[-1]

    def get_node_or_none(self) -> Node | None:
        if not self.nodes:
            return None
        return self.get_node()


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
