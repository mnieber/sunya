from sunya.utils import camel_to_kebab
from sunya.entities.utils.actor_to_str import actor_to_str


def get_actor_str(role_or_actor):
    from sunya.scenarios.models.role import Role
    from sunya.entities.models.entity import split_now_suffix

    if isinstance(role_or_actor, Role):
        return actor_to_str(role_or_actor)

    actor = role_or_actor
    parts = []
    key = actor_to_str(actor)
    key, suffix = split_now_suffix(key)

    for part in key.split(" "):
        parts.append(camel_to_kebab(part))
    return _shorten_term_str("-".join(parts)) + suffix


def _shorten_term_str(term_str):
    parts = term_str.split(":")
    if len(parts) > 1:
        suffix = parts[-1]
        if parts[-2].endswith(suffix):
            pos = parts[-2].rfind(suffix)
            parts[-2] = parts[-2][:pos]
    return ":".join(parts)
