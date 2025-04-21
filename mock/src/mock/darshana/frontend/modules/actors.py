import typing as T

from sunya import Entity

from kits.react_app.impl.entities import Component, ReactModule, Route


class Actors(ReactModule):
    class Types:
        class Actor(Entity):
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
