from sunya.actors.models.role import Role
from sunya.modules.utils.component_namespace import ActorSpec
from sunya.scenarios.models.scenario import get_scenario


def actor(actor: any, role: Role | None = None):
    if role is not None:
        role.actor = actor
        name = role.name

        if isinstance(actor, ActorSpec):
            current_node = get_scenario().get_node()
            if hasattr(current_node, "legend"):
                current_node.legend[name] = actor.full_path

    return "<remove_line/>"
