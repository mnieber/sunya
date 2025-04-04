from unittest.mock import MagicMock


def resolve_entity_in_global_namespace(name):
    if name and name[0].isupper():
        return MagicMock(name=name)

    return None
