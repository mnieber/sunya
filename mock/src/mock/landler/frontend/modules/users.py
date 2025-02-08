from sunya import Entity
from mock.react_app.namespace import ReactModule


class Users(ReactModule):
    class Types:
        class User(Entity):
            email: str
