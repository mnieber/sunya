from sunya.scenarios.models.role import Role, get_role


def add_role(name):
    from sunya.scenarios.models.store import get_store

    role = get_role(name)
    if role is not None:
        return role

    role = Role(name=name)
    get_store().roles.append(role)
    return role
