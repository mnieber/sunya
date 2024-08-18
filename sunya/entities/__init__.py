from dataclassy import dataclass
from sunya.entities.actor_to_str import actor_to_str
from sunya.utils import str_to_uuid


@dataclass(kw_only=True)
class Entity:
    pass


class GenericEntity(Entity):
    key: str = ""


class EntityWithId(Entity):
    @property
    def id(self):
        return str_to_uuid(actor_to_str(self))


@actor_to_str.method((GenericEntity,))
def generic_entity_to_str(generic_entity):
    return generic_entity.key
