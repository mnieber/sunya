from sunya.scenarios.preregistered_entity import PreregisteredEntity
from sunya.scenarios.store import store, get_key


def register(entity, preregistered_entity=None, name=None):
    if preregistered_entity:
        if not isinstance(preregistered_entity, PreregisteredEntity):
            raise ValueError("preregistered_entity must be of type PreregisteredEntity")
        if name:
            raise ValueError("Cannot specify both a name and a preregistering entity")
        name = preregistered_entity.name

    if not name:
        raise ValueError("Entity must be given a name")
    if name in store.scenario.entity_by_name:
        if not preregistered_entity:
            raise ValueError(f"Entity with name {name} already exists")
    store.scenario.entity_by_name[name] = entity

    key = get_key(entity)
    if key in store.scenario.entity_by_key:
        existing_entity = store.scenario.entity_by_key[key]
        if (
            existing_entity is not entity
            and existing_entity is not preregistered_entity
        ):
            raise ValueError(
                f"Entity with name {name} already registered under key {key}"
            )
    store.scenario.entity_by_key[key] = entity

    if preregistered_entity:
        # Register the fact that before this node, the entity did not yet exist
        for linked_node in preregistered_entity.linked_nodes:
            linked_node.pre_entity_memo_by_key[key] = None

            # Update node.fact to replace preregistered_entity with entity
            linked_node.fact = tuple(
                entity if fact_bit is preregistered_entity else fact_bit
                for fact_bit in linked_node.fact
            )

    return entity


def preregister(name: str):
    entity = PreregisteredEntity(name=name)
    store.scenario.entity_by_key[get_key(entity)] = entity
    store.scenario.entity_by_name[name] = entity
    return entity


def unregister(name):
    entity = store.scenario.entity_by_name.get(name)
    if not entity or isinstance(entity, PreregisteredEntity):
        return

    store.scenario.entity_by_name.pop(name)
    store.scenario.entity_by_key.pop(get_key(entity))
