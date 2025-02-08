import typing as T
from sunya.entities.utils.actor_to_str import actor_to_str


class Role:
    _name: str
    _actor: T.Any = None

    def __init__(self, name: str, actor=None):
        self._name = name
        self._actor = actor._actor if isinstance(actor, Role) else actor

    def __bool__(self):
        return bool(self._actor)

    def __eq__(self, other):
        if isinstance(other, Role):
            return self._name == other._name and self._actor == other._actor
        return False

    def __getattr__(self, name, *args, **kwargs):
        if name in ("_actor", "_name") or name.startswith("__"):
            return object.__getattribute__(self, name, *args, **kwargs)
        return getattr(self._actor, name)

    def __setattr__(self, name, value):
        if name in ("_actor", "_name") or name.startswith("__"):
            return object.__setattr__(self, name, value)
        if not hasattr(self._actor, name):
            raise AttributeError(f"{self._actor} has no attribute {name}")
        return setattr(self._actor, name, value)

    def __repr__(self):
        return f"{self._name}: {actor_to_str(self._actor) if self._actor else 'None'}"

    def __len__(self):
        return len(self._actor) if self._actor else 0

    def __iter__(self):
        return iter(self._actor)


@actor_to_str.method((Role,))
def role_to_str(role):
    return role._name


def get_role(name):
    from sunya.scenarios.models.store import get_store

    for role in get_store().roles:
        if role._name == name:
            return role

    return None
