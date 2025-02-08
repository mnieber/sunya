import typing as T
from copy import deepcopy

from dataclassy import dataclass
from sunya.nodes.models.tag import Tag

if T.TYPE_CHECKING:
    pass


@dataclass(kw_only=True)
class Fact:
    bits: T.Tuple = tuple()
    tags: T.List[Tag] = []

    def __post_init__(self):
        from sunya.scenarios.models.role import Role

        normalized_bits = tuple()
        for bit in self.bits:
            if not bit and not isinstance(bit, Role):
                raise ValueError(f"Empty fact bit in fact {self.bits}")
            normalized_bits += (deepcopy(bit),)

        self.bits = normalized_bits


def get_anchor(step):
    from sunya.scenarios.models.goal import Goal

    while step:
        for tag in step.fact.tags:
            if tag.name in ("The",):
                return step.fact.bits[tag.range[0] : tag.range[1]]
            if tag.name in ("CallsThe",):
                return ("the", *step.fact.bits[tag.range[0] + 1 : tag.range[1]])
        if isinstance(step, Goal):
            step = step.parent
        else:
            step = None
    return tuple()
