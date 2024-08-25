import typing as T

from dataclassy import Internal, dataclass
from sunya.entities import Entity
from sunya.scenarios.roles import Role

if T.TYPE_CHECKING:
    from sunya.scenarios.scenario import Scenario


@dataclass(kw_only=True)
class Node:
    scenario: "Scenario"
    name = "root"
    fact: T.Tuple
    nodes: T.List["Node"] = []
    level: int = 0
    pre_entity_memo_by_key: Internal[T.Dict] = {}
    post_entity_memo_by_key: Internal[T.Dict] = {}
    pre_entity_key_by_role_name: Internal[T.Dict] = {}
    post_entity_key_by_role_name: Internal[T.Dict] = {}
    is_finalized: bool = False

    def __post_init__(self):
        for fact_bit in self.fact:
            if not fact_bit:
                raise ValueError(f"Empty fact bit in fact {self.fact}")


class Step(Node):
    name = "step"


class Goal(Node):
    name = "goal"


def get_node_entity_and_role_pairs(node):
    from sunya.scenarios.store import get_key

    result = []
    keys = []

    def add_entity(entity, role):
        key = (get_key(entity), role.name if role else None)
        if key not in keys:
            keys.append(key)
            result.append((entity, role))

    for fact_bit in node.fact:
        if isinstance(fact_bit, Entity):
            add_entity(fact_bit, role=None)
        elif isinstance(fact_bit, Role):
            role = fact_bit
            if entity := node.scenario.get_entity_by_role(fact_bit.name):
                add_entity(entity, role)

    return result
