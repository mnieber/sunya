import typing as T
from sunya.scenarios.models.store import store

from dataclassy import dataclass
from sunya.entities.models.entity import Entity

if T.TYPE_CHECKING:
    from sunya.nodes.models.node import Node


@dataclass(kw_only=True)
class EntityRecord:
    name: str
    key: str
    entity: Entity


@dataclass(kw_only=True)
class Scenario:
    name: str
    root_node: "Node" = T.cast(T.Any, None)

    def __post_init__(self):
        from sunya.scenarios.actions.create_step import create_step

        self.root_node = create_step(scenario=self, parent_node=None, fact_bits=tuple())

    def get_list_of_nodes(self, node=None):
        result = [node] if node else []
        source_node = node or self.root_node
        for child_node in source_node.nodes:
            for s in self.get_list_of_nodes(child_node):
                result.append(s)

        return result


def get_scenario(name: str):
    for scenario in store.scenarios:
        if scenario.name == name:
            return scenario
    return None
