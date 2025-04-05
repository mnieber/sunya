from dataclassy import dataclass
import typing as T

if T.TYPE_CHECKING:
    from .config_node import ConfigNode


@dataclass
class RootConfigNode:
    label: str
    child_nodes: T.List[ConfigNode] = []
