from sunya.scenarios.models.scenario import Scenario
from sunya.nodes.models.diagram_node import DiagramNode


def add_markdown_node(scenario: Scenario, node_title: str) -> DiagramNode:
    diagram_node = DiagramNode(title=node_title)
    scenario.nodes.append(diagram_node)

    return diagram_node
