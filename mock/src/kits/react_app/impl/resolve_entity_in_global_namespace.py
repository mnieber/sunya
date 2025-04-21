from unittest.mock import MagicMock

import kits.react_app.impl.namespace as F
from kits.react_app.impl.entities import Route


def resolve_entity_in_global_namespace(name):
    if name == "frontend":
        return F.Frontend()

    if name == "organization_route":
        return Route(name="organization")

    if name and name[0].isupper():
        return MagicMock(name=name)

    return None
