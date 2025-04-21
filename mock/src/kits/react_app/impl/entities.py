from sunya import Entity
from sunya.utils import type_name_to_kebab
import typing as T


class Frontend(Entity):
    pass


class Route(Entity):
    name: T.Optional[str] = None

    @property
    def name_or_default_name(self):
        default_name = type_name_to_kebab(self)
        if default_name.endswith("-route"):
            default_name = default_name[:-6]
        return self.name or default_name


class Form(Entity):
    name: str
    data: dict = {}


class ReactModule(Entity):
    pass


class Mutation(Entity):
    pass


class Query(Entity):
    pass


class Component(Entity):
    pass


class State(Entity):
    pass


class Ctr(Entity):
    pass


class Action(Entity):
    name: str


class Facet(Entity):
    name: str
