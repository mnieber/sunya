import typing as T

from dataclassy import Internal, dataclass
from sunya.entities import Entity


@dataclass(kw_only=True)
class Step:
    fact: T.Tuple
    steps: T.List["Step"] = []
    level: int
    pre_entity_memo_by_key: Internal[T.Dict] = {}
    post_entity_memo_by_key: Internal[T.Dict] = {}

    @property
    def entities(self):
        return [x for x in self.fact if isinstance(x, Entity)]

    def __post_init__(self):
        for fact_bit in self.fact:
            if not fact_bit:
                raise ValueError(f"Empty fact bit in fact {self.fact}")
