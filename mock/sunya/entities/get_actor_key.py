from multimethods import Default, MultiMethod
from sunya.entities.actor_to_str import actor_to_str


def dispatch_get_actor_key(x):
    return (type(x),)


get_actor_key = MultiMethod("get_actor_key", dispatch_get_actor_key)


@get_actor_key.method(Default)
def get_default_actor_key(x):
    return actor_to_str(x)
