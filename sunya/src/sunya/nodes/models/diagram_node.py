
from dataclassy import dataclass
from sunya.nodes.models.node import Node


@dataclass(kw_only=True)
class DiagramNode(Node):
    title: str
    markdown: str = ""
