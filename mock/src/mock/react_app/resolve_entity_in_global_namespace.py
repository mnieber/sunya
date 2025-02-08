import mock.react_app.namespace as F
from mock.react_app.entities import Route
from unittest.mock import MagicMock


def resolve_entity_in_global_namespace(name):
    if name == "frontend":
        return F.Frontend()

    if name == "organization_route":
        return Route(name="organization")

    if name and name[0].isupper():
        return MagicMock(name=name)

    return None
