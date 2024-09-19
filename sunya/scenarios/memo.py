import copy
from sunya.entities import Entity
from sunya.entities.actor_to_str import get_actor_str
from sunya.scenarios.roles import Role


def create_memo(entity):
    memo = {}
    for field, value in _iter_fields(entity):
        if isinstance(value, list):
            memo_value = [_get_memo_field_value(x) for x in value]
        elif isinstance(value, dict):
            memo_value = {k: _get_memo_field_value(v) for k, v in value.items()}
        else:
            memo_value = _get_memo_field_value(value)

        memo[field] = memo_value
    return memo


def _get_memo_field_value(x):
    if isinstance(x, Entity):
        return get_actor_str(x)

    if isinstance(x, Role):
        if isinstance(x.actor, Entity):
            return get_actor_str(x.actor)
        return x.name

    return copy.deepcopy(x)


def _iter_fields(obj):
    for name in dir(obj):
        if not name.startswith("__"):
            yield name, getattr(obj, name)
