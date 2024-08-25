from sunya.scenarios.store import store, get_key
from sunya.scenarios.scenario import EntityRecord
from sunya.scenarios.roles import add_role, get_role


def add_actor(entity, name, role=None):
    if store.scenario.get_entity_by_name(name):
        raise ValueError(f"Entity with name {name} already exists")

    key = get_key(entity)
    if existing_entity := store.scenario.get_entity_by_key(key):
        if existing_entity is not entity:
            raise ValueError(
                f"Entity with name {name} already registered under key {key}"
            )

    store.scenario.update_entity_record(
        EntityRecord(entity=entity, name=name, role=role, key=key)
    )
    if role:
        role = get_role(role) or add_role(role)
        role.add_entity(entity)

    return entity
