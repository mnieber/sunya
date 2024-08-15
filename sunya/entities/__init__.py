from dataclassy import dataclass
from sunya.entities.actor_to_str import actor_to_str
from sunya.utils import type_name_to_kebab, str_to_uuid


@dataclass(kw_only=True)
class Entity:
    pass


class EntityWithId(Entity):
    @property
    def id(self):
        return str_to_uuid(actor_to_str(self))


@dataclass(kw_only=True)
class Value:
    pass


class List(Entity):
    name: str
    items: list = []


class Fn(Entity):
    name: str = ""

    def __post_init__(self):
        self.name = self.name or type_name_to_kebab(self)


@actor_to_str.method((Fn,))
def fn_to_str(fn):
    return f"{fn.name}+:function"


@actor_to_str.method((List,))
def list_to_str(list):
    return f"{list.name}+:list"
