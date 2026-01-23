from mock.default.stack.namespace import Module
from sunya import EntityWithId


class Users(Module):
    class Types:
        class User(EntityWithId):
            email: str
