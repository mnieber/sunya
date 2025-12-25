from sunya.actors.models.role import Role


def participant(actor: any, role: Role | None = None):
    if role is not None:
        role.actor = actor
        name = role.name
    else:
        name = actor.__class__.__name__

    actor_name = name

    postfixes = ["ApiView", "Action", "Rule"]
    for postfix in postfixes:
        if actor_name.endswith(postfix):
            actor_name = actor_name[: -len(postfix)] + "<br/>" + postfix
            break

    return f"participant {name} as {actor_name}"
