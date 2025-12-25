from sunya.actors.actions.add_role import add_role
from sunya.actors.models.role import Role


class RoleNamespace:
    def __getattr__(self, name) -> Role:
        return add_role(name)

    def __setattr__(self, name, value):
        actor = value.actor if isinstance(value, Role) else value
        add_role(name).actor = actor


R = RoleNamespace()
