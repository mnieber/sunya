from sunya.actors.models.role import Role
from sunya.scenarios.utils.module_namespace import ActorSpec
from sunya.scenarios.models.scenario import get_scenario


def participant(actor: any, role: Role | None = None):
    if role is not None:
        role.actor = actor
        name = role.name

        # If the actor is an ActorSpec, add it to the current node's legend
        if isinstance(actor, ActorSpec):
            current_node = get_scenario().get_node()
            if hasattr(current_node, "legend"):
                current_node.legend[name] = actor.full_path
    else:
        name = actor.__class__.__name__

    actor_name = name

    postfixes = ["ApiView", "Action", "Rule"]
    for postfix in postfixes:
        if actor_name.endswith(postfix):
            actor_name = actor_name[: -len(postfix)] + "<br/>" + postfix
            break

    return f"participant {name} as {actor_name}"
