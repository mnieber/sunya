import typing as T

from dataclassy import Internal, dataclass
from sunya.entities import Entity


@dataclass(kw_only=True)
class Node:
    fact: T.Tuple
    nodes: T.List["Node"] = []
    level: int
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
    pass


class Goal(Node):
    pass
