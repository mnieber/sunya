from sunya.scenarios.store import get_key


def get_entity_delta(node, entity):
    if not node.is_finalized:
        raise NodeNotFinalizedError(node)

    key = get_key(entity)
    pre_entity_memo = node.pre_entity_memo_by_key.get(key)
    post_entity_memo = node.post_entity_memo_by_key.get(key)

    delta = dict()
    for field, value in (post_entity_memo or dict()).items():
        existing_value = (
            pre_entity_memo.get(field, NoValue) if pre_entity_memo else NoValue
        )
        delta[field] = (existing_value, value)
    return delta


class NoValue:
    pass


class NodeNotFinalizedError(Exception):
    def __init__(self, node):
        self.node = node
        super().__init__(f"Node {node} has not been finalized")
