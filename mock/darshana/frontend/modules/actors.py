from darshana.stack.namespace import Module
from darshana.frontend.entities import Component, Route
from sunya import actor_to_str, G as g, EntityWithId
import typing as T


class Actors(Module):
    class Types:
        class Actor(EntityWithId):
            name: str
            fields: T.Dict[str, T.Any]
            changed_fields: T.List[str]

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


@actor_to_str.method((Actors.Types.Actor,))
def actor_to_str(actor):
    return f"{actor.name}+:actor"
