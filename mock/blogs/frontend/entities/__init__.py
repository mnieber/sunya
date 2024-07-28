from sunya import Entity, actor_to_str
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


class Mutation(Entity):
    pass


class Query(Entity):
    pass


class Component(Entity):
    pass


class Facet(Entity):
    name: str


class Trim(Entity):
    name: str


frontend = Frontend()


@actor_to_str.method((Frontend,))
def frontend_to_str(frontend):
    return f":frontend"


@actor_to_str.method((Mutation,))
def mutation_to_str(mutation):
    return f":mutation"


@actor_to_str.method((Route,))
def route_to_str(route):
    return f"{route.name_or_default_name}+:route"


@actor_to_str.method((Component,))
def component_to_str(component):
    return f"{type_name_to_kebab(component)}:component"
