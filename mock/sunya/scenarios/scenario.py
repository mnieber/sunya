import typing as T

from dataclassy import dataclass
from sunya.entities import Entity
from sunya.scenarios.node import Node


@dataclass(kw_only=True)
class Scenario:
    name: str
    entity_by_key: T.Dict[T.Tuple, Entity] = {}
    entity_by_name: T.Dict[T.Tuple, Entity] = {}
    root_node: Node

    def get_entity(self, entity_class, **kwargs):
        for entity in self.entity_by_key.values():
            if isinstance(entity, entity_class):
                found = True
                for key, value in kwargs.items():
                    if getattr(entity, key) != value:
                        found = False
                        break
                if found:
                    return entity
        return None

    def get_entity_by_name(self, name):
        return self.entity_by_name.get(name, None)

    def get_list_of_nodes(self, node=None):
        result = [node] if node else []
        source_node = node or self.root_node
        for child_node in source_node.nodes:
            for s in self.get_list_of_nodes(child_node):
                result.append(s)

        return result
