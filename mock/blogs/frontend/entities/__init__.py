from sunya import Entity, actor_to_str
from sunya.utils import camel_to_kebab, get_type_name, l0


class Frontend(Entity):
    pass


class Route(Entity):
    name: str

    @property
    def name_or_default_name(self):
        return self.name or camel_to_kebab(l0(get_type_name(self)))


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
    return f"{route.name_or_default_name}+:route"
