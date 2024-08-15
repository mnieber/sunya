import typing as T

from dataclassy import Internal, dataclass
from sunya import actor_to_str
from sunya.scenarios.node import Node


@dataclass(kw_only=True)
class PreregisteredEntity:
    name: str
    linked_nodes: Internal[T.List[Node]] = []


@actor_to_str.method((PreregisteredEntity,))
def preregistered_entity_to_str(preregistered_entity):
    return f"{preregistered_entity.name}:preregistered_entity"
