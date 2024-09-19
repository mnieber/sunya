from default.stack.namespace import Module
from default.frontend.entities import Component, Route
from sunya import actor_to_str, EntityWithId, G as g, GenericEntity

import typing as T


class Actors(Module):
    class Types:
        class Actor(EntityWithId):
            key: str
            fields: T.Dict[str, T.Any] = {}
            changed_fields: T.List[str] = []

    class Routes:
        class Actor(Route):
            pass

    class Views:
        class ActorView(Component):
            pass

    class Components:
        class ActorLink(Component):
            pass


g.actor_view = Actors.Views.ActorView()
g.actor_route = Actors.Routes.Actor()
g.actor_link = Actors.Components.ActorLink()
g.field_delta_set = GenericEntity(_key=":field_delta_set")
g.actor = Actors.Types.Actor(key="")


@actor_to_str.method((Actors.Types.Actor,))
def actor_to_str(actor):
    name = actor.key.replace(":", "-").replace("+", "-")
    return f"{name}+:actor"
