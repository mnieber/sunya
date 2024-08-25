from sunya import Entity, actor_to_str, G as g
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


class State(Entity):
    pass


class Ctr(Entity):
    pass


class Action(Entity):
    name: str


class Facet(Entity):
    name: str


g.frontend = Frontend()


@actor_to_str.method((Frontend,))
def frontend_to_str(frontend):
    return f":frontend"


@actor_to_str.method((Query,))
def query_to_str(query):
    return f"{type_name_to_kebab(query)}:query"


@actor_to_str.method((Mutation,))
def mutation_to_str(mutation):
    return f"{type_name_to_kebab(mutation)}:mutation"


@actor_to_str.method((State,))
def state_to_str(state):
    return f"{type_name_to_kebab(state)}:state"


@actor_to_str.method((Ctr,))
def ctr_to_str(ctr):
    return f"{type_name_to_kebab(ctr)}:ctr"


@actor_to_str.method((Route,))
def route_to_str(route):
    return f"{route.name_or_default_name}+:route"


@actor_to_str.method((Component,))
def component_to_str(component):
    return f"{type_name_to_kebab(component)}:component"


@actor_to_str.method((Action,))
def action_to_str(action):
    return f"{action.name}:action"
