import typing as T

from dataclassy import dataclass

if T.TYPE_CHECKING:
    from sunya.scenarios.models.scenario import Scenario


@dataclass(kw_only=True)
class Store:
    scenarios: T.List["Scenario"] = []
    stack: T.List = []
    roles: T.List = []

    @property
    def scenario(self):
        return self.scenarios[-1]

    @property
    def node(self):
        return self.stack[-1]


store = Store()


def get_store():
    global store
    return store
