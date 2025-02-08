from sunya.scenarios.models.store import get_store
from sunya.nodes.models.node import Node
from sunya.scenarios.models.scenario_context import get_scenario_context


class NodeContext:
    def __init__(self, node: Node):
        self.node = node

    @classmethod
    def enter(cls, node):
        result = get_store().stack.append(node)
        # Call implement_step to allow the scenario context to take a special
        # action when entering the node, such as registering certain actors.
        get_scenario_context().implement_step(node)
        return result

    @classmethod
    def exit(cls):
        get_store().stack.pop()

    def __enter__(self):
        return self.enter(self.node)

    def __exit__(self, *args):
        self.exit()
