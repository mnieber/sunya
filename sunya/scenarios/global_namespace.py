from sunya.scenarios.store import store
import typing as T
from sunya.scenarios.roles import add_role, get_role


class GlobalNamespace:
    def __init__(self):
        self._attributes = {}

    def __setattr__(self, name, value):
        if name == "_attributes":
            super().__setattr__(name, value)
        elif name in self._attributes:
            raise AttributeError(f"Attribute '{name}' already exists")
        else:
            self._attributes[name] = value

    def __getattr__(self, name):
        if entity := store.scenario.get_entity_by_name(name):
            return T.cast(T.Any, entity)

        if name in self._attributes:
            return T.cast(T.Any, self._attributes[name])

        if role := get_role(name):
            return T.cast(T.Any, role)

        if name[0].isupper():
            return T.cast(T.Any, add_role(name))

        raise AttributeError(f"Attribute '{name}' does not exist")


G = GlobalNamespace()
