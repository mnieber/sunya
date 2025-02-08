from sunya.nodes.actions.create_node import create_node
from sunya.scenarios.models.step import Step


def create_step(scenario, parent_node, fact_bits):
    return create_node(Step, scenario, parent_node, fact_bits)
