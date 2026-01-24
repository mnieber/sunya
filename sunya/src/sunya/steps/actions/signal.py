from sunya.steps.models.message import Message
from sunya.steps.rules.self import Self


def signal(from_actor: any, to_actor: any, dashed=False):
    if isinstance(to_actor, Self):
        to_actor = from_actor

    return Message(from_actor, to_actor, dashed)
