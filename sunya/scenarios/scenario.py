import typing as T

from dataclassy import dataclass
from sunya.entities import Entity
from sunya.scenarios.node import Node


@dataclass(kw_only=True)
class EntityRecord:
    name: str
    key: str
    role: str
    entity: Entity


@dataclass(kw_only=True)
class Scenario:
    name: str
    entity_records: T.List[EntityRecord] = []
    root_node: Node = T.cast(T.Any, None)

    def __post_init__(self):
        self.root_node = Node(scenario=self, fact=tuple(), level=0)

    def update_entity_record(self, entity_record):
        for i, existing_entity_record in enumerate(self.entity_records):
            if existing_entity_record.name == entity_record.name:
                self.entity_records[i] = entity_record
                return

        self.entity_records.append(entity_record)

    def get_entity_by_name(self, name):
        for entity_record in self.entity_records:
            if entity_record.name == name:
                return entity_record.entity
        return None

    def get_entity_by_key(self, key):
        for entity_record in self.entity_records:
            if entity_record.key == key:
                return entity_record.entity
        return None

    def get_entity_by_role(self, role):
        for entity_record in self.entity_records:
            if entity_record.role == role:
                return entity_record.entity
        return None

    def get_list_of_nodes(self, node=None):
        result = [node] if node else []
        source_node = node or self.root_node
        for child_node in source_node.nodes:
            for s in self.get_list_of_nodes(child_node):
                result.append(s)

        return result
