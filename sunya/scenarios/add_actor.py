from sunya.scenarios.store import store, get_key
from sunya.scenarios.scenario import EntityRecord


def add_actor(entity, name):
    if store.scenario.get_entity_by_name(name):
        raise ValueError(f"Entity with name {name} already exists")

    key = get_key(entity)
    if existing_entity := store.scenario.get_entity_by_key(key):
        if existing_entity is not entity:
            raise ValueError(
                f"Entity with name {name} already registered under key {key}"
            )

    store.scenario.update_entity_record(EntityRecord(entity=entity, name=name, key=key))

    return entity
