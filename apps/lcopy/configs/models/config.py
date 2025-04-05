from dataclassy import dataclass
import typing as T

if T.TYPE_CHECKING:
    from .root_config_node import RootConfigNode


@dataclass
class Config:
    # List of other lcopy configs to include
    include: T.List[str] = []
    # List of root configuration nodes
    root_config_nodes: T.List[RootConfigNode] = []
