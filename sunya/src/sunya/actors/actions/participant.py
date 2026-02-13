import re

from sunya.actors.models.role import Role
from sunya.modules.utils.module_namespace import ActorSpec
from sunya.scenarios.models.scenario import get_scenario


def participant(actor: any, role: Role | None = None):
    scenario = get_scenario()

    if role is not None:
        role.actor = actor
        name = role.name

        # If the actor is an ActorSpec, add it to the current node's legend
        if isinstance(actor, ActorSpec):
            current_node = scenario.get_node()
            if hasattr(current_node, "legend"):
                current_node.legend[name] = actor.full_path
    else:
        name = actor.__class__.__name__

    actor_name = _create_actor_name(name)
    scenario.get_node().participants.append(name)

    return f"participant {name} as {actor_name}"


def _create_actor_name(name):
    # Split the name into camel-case parts
    parts = re.findall(r"[A-Z]+(?=[A-Z][a-z]|\b)|[A-Z][a-z]+|[a-z]+|[0-9]+", name)
    if not parts:
        return name

    # Group parts into lines that fit within the length limit
    MAX_LINE_LENGTH = 15
    lines = []
    current_line = ""

    for part in parts:
        if not current_line:
            current_line = part
        elif len(current_line) + len(part) <= MAX_LINE_LENGTH:
            current_line += part
        else:
            lines.append(current_line)
            current_line = part

    if current_line:
        lines.append(current_line)

    return "<br/>".join(lines)
