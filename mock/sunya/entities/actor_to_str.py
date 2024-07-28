from multimethods import MultiMethod
from sunya.utils import camel_to_kebab


def dispatch_actor_to_str(x):
    return (type(x),)


actor_to_str = MultiMethod("actor_to_str", dispatch_actor_to_str)


def shorten_term_str(term_str):
    parts = term_str.split(":")
    if len(parts) > 1:
        suffix = parts[-1]
        if parts[-2].endswith(suffix):
            pos = parts[-2].rfind(suffix)
            parts[-2] = parts[-2][:pos]
    return ":".join(parts)


def get_actor_str(actor):
    parts = []
    for part in actor_to_str(actor).split(" "):
        parts.append(camel_to_kebab(part))
    return shorten_term_str("-".join(parts))
