from sunya.actors.models.role import Role


def actor(actor: any, role: Role | None = None):
    if role is not None:
        role.actor = actor
    return "<remove_line/>"
