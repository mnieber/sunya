from sunya.nodes.actions.create_node import create_node
from sunya.scenarios.models.goal import Goal


def create_goal(scenario, parent_node, fact_bits):
    return create_node(Goal, scenario, parent_node, fact_bits)
