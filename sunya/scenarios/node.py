import typing as T

from dataclassy import Internal, dataclass

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
    pre_actor_key_by_role_name: Internal[T.Dict] = {}
    post_entity_memo_by_key: Internal[T.Dict] = {}
    post_actor_key_by_role_name: Internal[T.Dict] = {}
    is_finalized: bool = False

    def __post_init__(self):
        for fact_bit in self.fact:
            if not fact_bit:
                raise ValueError(f"Empty fact bit in fact {self.fact}")


class Step(Node):
    name = "step"


class Goal(Node):
    name = "goal"
