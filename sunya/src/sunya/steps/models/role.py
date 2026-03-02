import typing as T


class Role:
    _name: str
    _actor: T.Any = None

    def __init__(self, name: str, actor=None):
        self._name = name
        self._actor = actor.actor if isinstance(actor, Role) else actor

    def __bool__(self):
        return bool(self.actor)

    @property
    def name(self):
        return self._name

    @property
    def actor(self):
        return self._actor

    @actor.setter
    def actor(self, value):
        if self._actor:
            if self._actor != value:
                raise CannotMutateRoleError(
                    f"Role '{self._name}' is already assigned to an actor."
                )
        else:
            self._actor = value

    def __repr__(self):
        return f"{self.name}"


def get_role(name):
    from sunya.scenarios.models.scenario import get_scenario

    for role in get_scenario().roles:
        if role.name == name:
            return role

    return None


class CannotMutateRoleError(Exception):
    pass
