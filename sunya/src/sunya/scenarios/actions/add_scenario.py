from sunya.scenarios.models.store import store
from sunya.scenarios.models.scenario import Scenario


def add_scenario(name: str):
    scenario = Scenario(name=name)
    store.scenarios.append(scenario)

    return scenario
