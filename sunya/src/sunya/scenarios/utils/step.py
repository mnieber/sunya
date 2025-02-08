from sunya.nodes.actions.add_node import add_node
from sunya.nodes.utils.node_context import NodeContext
from sunya.scenarios.actions.create_step import create_step
from sunya.scenarios.models.store import get_store


def step(*fact_bits):
    node = add_node(
        create_step(get_store().scenario, get_store().node, fact_bits=fact_bits)
    )
    return NodeContext(node)
