from sunya.scenarios.store import store
import typing as T
from sunya.scenarios.register import preregister


class EntityLookup:
    def __getattr__(self, name):
        if entity := store.scenario.get_entity_by_name(name):
            return T.cast(T.Any, entity)

        return T.cast(T.Any, preregister(name))


def get_entities():
    return EntityLookup()
