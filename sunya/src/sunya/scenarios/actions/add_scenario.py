from sunya.scenarios.models.store import store
from sunya.nodes.utils.node_context import NodeContext
from sunya.scenarios.models.scenario import Scenario


def add_scenario(name: str):
    scenario = Scenario(name=name)
    store.scenarios.append(scenario)

    return NodeContext(scenario.root_node)
