from sunya.scenarios.models.store import get_store


def add_node(node):
    get_store().node.nodes.append(node)
    return node
