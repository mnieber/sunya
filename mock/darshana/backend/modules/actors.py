from default.stack.namespace import Module, Form
from default.backend.namespace import Action

from sunya import EntityWithId, actor_to_str, G as g


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


g.create_actor_action = Actors.Actions.CreateActor()


@actor_to_str.method((Actors.Models.Actor,))
def actor_to_str(actor):
    name = actor.key.replace(":", "-").replace("+", "-")
    return f"{name}+:actor"
