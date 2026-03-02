from sunya.roles.models.role import Role, get_role
from sunya.scenarios.models.scenario import get_scenario


def add_role(name):
    role = get_role(name)
    if role is not None:
        return role

    role = Role(name=name)
    get_scenario().roles.append(role)
    return role
