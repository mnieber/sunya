import typing as T

from dataclassy import dataclass
from sunya.nodes.models.fact import Fact

if T.TYPE_CHECKING:
    from sunya.scenarios.models.scenario import Scenario


@dataclass(kw_only=True)
class Node:
    scenario: "Scenario"
    name = "root"
    fact: Fact
    nodes: T.List["Node"] = []
    parent: T.Optional["Node"] = None
    level: int = 0
