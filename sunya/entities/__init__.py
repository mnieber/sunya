from dataclassy import dataclass
from sunya.entities.actor_to_str import actor_to_str
from sunya.utils import str_to_uuid
import datetime
from sunya.utils import get_time


@dataclass(kw_only=True)
class Entity:
    pass


class GenericEntity(Entity):
    _key: str = ""


class EntityWithId(Entity):
    @property
    def id(self):
        key = actor_to_str(self)
        if "@@" in key:
            key = key.split("@@")[0]
        return str_to_uuid(key)


class NowMixin:
    __now__: datetime.datetime = get_time.now(bump=False)


def get_now_suffix(entity):
    return f"@@{entity.__now__}" if entity.__now__ else ""


def split_now_suffix(key):
    if "@@" in key:
        key, suffix = key.split("@@")
        suffix = f"@@{suffix}"
    else:
        suffix = ""

    return key, suffix


@actor_to_str.method((GenericEntity,))
def generic_entity_to_str(generic_entity):
    return generic_entity._key
