from copy import deepcopy


def at_ts(entity, ts):
    entity_at_ts = deepcopy(entity)
    entity_at_ts._now_ = ts
    return entity_at_ts
