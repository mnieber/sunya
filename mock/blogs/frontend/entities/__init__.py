from sunya import Entity, actor_to_str
from sunya.utils.case import get_type_name


class Frontend(Entity):
    pass


class Route(Entity):
    pass


class Mutation(Entity):
    pass


class Query(Entity):
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
    return f"{get_type_name(route)}+:route"
