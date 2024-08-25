from dataclassy import dataclass
from sunya.entities import Entity
from sunya.entities.actor_to_str import actor_to_str
import typing as T


@dataclass(kw_only=True)
class Role:
    name: str
    entities: T.List[Entity] = []

    def add_entity(self, entity):
        from sunya.scenarios.store import get_key

        key = get_key(entity)
        if not next((e for e in self.entities if get_key(e) == key), None):
            self.entities.append(entity)


@actor_to_str.method((Role,))
def role_to_str(role):
    return role.name


def add_role(name):
    from sunya.scenarios.store import store

    if role := get_role(name):
        return role

    role = Role(name=name)
    store.roles.append(role)
    return role


def get_role(name):
    from sunya.scenarios.store import store

    for role in store.roles:
        if role.name == name:
            return role

    return None
