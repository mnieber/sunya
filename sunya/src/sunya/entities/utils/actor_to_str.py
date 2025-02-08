from multimethods import MultiMethod, Default


def dispatch_actor_to_str(x):
    return (type(x),)


actor_to_str = MultiMethod("actor_to_str", dispatch_actor_to_str)


@actor_to_str.method(Default)
def default_to_str(actor):
    return f"?:{actor.__class__.__name__}"
