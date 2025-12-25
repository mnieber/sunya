import typing as T

from dataclassy import dataclass

if T.TYPE_CHECKING:
    from sunya.scenarios.models.scenario import Scenario


@dataclass(kw_only=True)
class Store:
    scenarios: T.List["Scenario"] = []

    @property
    def scenario(self):
        return self.scenarios[-1]


store = Store()


def get_store():
    global store
    return store
