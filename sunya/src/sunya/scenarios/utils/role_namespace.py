from sunya.scenarios.actions.add_role import add_role
from sunya.scenarios.models.role import Role


class RoleNamespace:
    def __getattr__(self, name):
        return add_role(name)

    def __setattr__(self, name, value):
        actor = value._actor if isinstance(value, Role) else value
        add_role(name)._actor = actor


R = RoleNamespace()
