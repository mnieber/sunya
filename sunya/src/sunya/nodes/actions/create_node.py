from sunya.nodes.models.fact import Fact
from sunya.nodes.rules.get_expanded_fact_bits import get_expanded_fact_bits


def create_node(klass, scenario, parent_node, fact_bits):
    expanded_fact_bits, tags = get_expanded_fact_bits(fact_bits, parent_node)

    return klass(
        scenario=scenario,
        fact=Fact(bits=tuple(expanded_fact_bits), tags=tags),
        nodes=[],
        parent=parent_node,
        level=parent_node.level + 1 if parent_node else 0,
    )
