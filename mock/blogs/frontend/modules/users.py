from blogs.stack.entities import Module
from sunya import EntityWithId


class Users(Module):
    class Types:
        class User(EntityWithId):
            email: str
