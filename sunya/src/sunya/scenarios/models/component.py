import typing as T

from dataclassy import dataclass

if T.TYPE_CHECKING:
    from sunya.scenarios.models.scenario import Scenario


@dataclass(kw_only=True)
class Component:
    name: str
    scenarios: T.List["Scenario"] = []

    @property
    def scenario(self):
        return self.scenarios[-1]
