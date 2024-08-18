from darshana.stack.namespace import Module
from darshana.frontend.entities import Component, Route
from sunya import actor_to_str, G as g, EntityWithId, GenericEntity

import typing as T


class Actors(Module):
    class Types:
        class Actor(EntityWithId):
            key: str
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
g.reconstructed_actor = Actors.Types.Actor(key="reconstructed")
g.field_delta_set = GenericEntity(key=":field_delta_set")


@actor_to_str.method((Actors.Types.Actor,))
def actor_to_str(actor):
    return f"{actor.name}+:actor"
