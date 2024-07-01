from multimethods import MultiMethod


def dispatch_actor_to_str(x):
    return (type(x),)


actor_to_str = MultiMethod("actor_to_str", dispatch_actor_to_str)
