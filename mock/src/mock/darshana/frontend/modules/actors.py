from mock.default.stack.namespace import Module
from mock.default.frontend.entities import Component, Route
from sunya import EntityWithId

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
