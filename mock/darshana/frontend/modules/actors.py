from darshana.stack.namespace import Module
from sunya import actor_to_str
import typing as T


class Actors(Module):
    class Types:
        class Actor(T.TypedDict):
            name: str
            fields: T.Dict[str, T.Any]
            changed_fields: T.List[str]

    class Views:
        class ActorView:
            pass

    class Components:
        class ActorLink:
            pass


@actor_to_str.method((Actors.Types.Actor,))
def actor_to_str(actor):
    return f"{actor.name}+:actor"
