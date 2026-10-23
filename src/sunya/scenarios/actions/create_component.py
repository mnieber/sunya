from sunya.scenarios.models.component import Component
from sunya.scenarios.models.store import get_store


def create_component(component_name: str):
    get_store().components.append(Component(name=component_name))
