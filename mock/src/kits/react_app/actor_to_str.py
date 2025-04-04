from sunya import actor_to_str
from sunya.utils.case import type_name_to_kebab
import kits.react_app.entities as E


@actor_to_str.method((E.Frontend,))
def frontend_to_str(frontend):
    return f":frontend"


@actor_to_str.method((E.Query,))
def query_to_str(query):
    return f"{type_name_to_kebab(query)}:query"


@actor_to_str.method((E.Mutation,))
def mutation_to_str(mutation):
    return f"{type_name_to_kebab(mutation)}:mutation"


@actor_to_str.method((E.State,))
def state_to_str(state):
    return f"{type_name_to_kebab(state)}:state"


@actor_to_str.method((E.Ctr,))
def ctr_to_str(ctr):
    return f"{type_name_to_kebab(ctr)}:ctr"


@actor_to_str.method((E.Route,))
def route_to_str(route):
    return f"{route.name_or_default_name}+:route"


@actor_to_str.method((E.Component,))
def component_to_str(component):
    return f"{type_name_to_kebab(component)}:component"


@actor_to_str.method((E.Action,))
def action_to_str(action):
    return f"{action.name}:action"
