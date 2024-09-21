from copy import deepcopy


def at_ts(entity, ts):
    entity_at_ts = deepcopy(entity)
    entity_at_ts.__now__ = ts
    return entity_at_ts
