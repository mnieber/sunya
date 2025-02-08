from sunya.entities.utils.actor_to_str import actor_to_str
from sunya.entities.models.entity import Entity


class GenericEntity(Entity):
    _key: str = ""


@actor_to_str.method((GenericEntity,))
def generic_entity_to_str(generic_entity):
    return generic_entity._key
