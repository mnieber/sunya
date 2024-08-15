import typing as T

from dataclassy import Internal, dataclass
from sunya.entities import Entity


@dataclass(kw_only=True)
class Node:
    name = "root"
    fact: T.Tuple
    nodes: T.List["Node"] = []
    level: int = 0
    pre_entity_memo_by_key: Internal[T.Dict] = {}
    post_entity_memo_by_key: Internal[T.Dict] = {}
    is_finalized: bool = False

    @property
    def entities(self):
        return [x for x in self.fact if isinstance(x, Entity)]

    def __post_init__(self):
        for fact_bit in self.fact:
            if not fact_bit:
                raise ValueError(f"Empty fact bit in fact {self.fact}")


class Step(Node):
    name = "step"


class Goal(Node):
    name = "goal"
