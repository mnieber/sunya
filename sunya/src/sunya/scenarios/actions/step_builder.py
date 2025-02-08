from sunya.nodes.rules.the import CallsThe
from sunya.nodes.utils.node_context import NodeContext


class StepBuilder:
    def __init__(self, fact_bits=None):
        self.fact_bits = fact_bits or tuple()

    def __getattr__(self, name):
        def relates_to(other_entity=None):
            if name == "calls_the" and other_entity:
                self.fact_bits = (*self.fact_bits, CallsThe(other_entity))
            else:
                self.fact_bits = (
                    *self.fact_bits,
                    name,
                    *([] if other_entity is None else [other_entity]),
                )

            return self

        return relates_to

    def __enter__(self):
        from sunya.scenarios.models.store import get_store
        from sunya.nodes.actions.add_node import add_node
        from sunya.scenarios.actions.create_step import create_step

        node = add_node(
            create_step(get_store().scenario, get_store().node, self.fact_bits)
        )
        return NodeContext.enter(node)

    def __exit__(self, *args):
        return NodeContext.exit()

    def __iter__(self):
        return iter(self.fact_bits)
