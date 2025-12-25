from sunya import Entity
from kits.react_app.impl.namespace import ReactModule


class Users(ReactModule):
    class Types:
        class User(Entity):
            email: str
