from mock.default.stack.namespace import Module, Form
from mock.default.backend.namespace import Action

from sunya import EntityWithId


class Actors(Module):
    class Models:
        class Actor(EntityWithId):
            key: str

    class Actions:
        class CreateActor(Action):
            class Args:
                create_actor_form: Form

    class DomainEvents:
        pass
