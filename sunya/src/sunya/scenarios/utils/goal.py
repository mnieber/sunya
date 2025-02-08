from sunya.nodes.actions.add_node import add_node
from sunya.scenarios.actions.create_goal import create_goal
from sunya.nodes.utils.node_context import NodeContext
from sunya.scenarios.models.store import get_store


def goal(fact_bits):
    node = add_node(
        create_goal(get_store().scenario, get_store().node, fact_bits=tuple(fact_bits))
    )
    return NodeContext(node)
