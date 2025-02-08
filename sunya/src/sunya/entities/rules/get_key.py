from sunya.entities.rules.get_actor_str import get_actor_str


def get_key(entity):
    return (entity.__class__, get_actor_str(entity))
