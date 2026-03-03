import typing as T

from dataclassy import dataclass
from sunya.steps.models.rel import Rel


@dataclass(kw_only=True)
class Step:
    rel: Rel

    # These are the child steps
    steps: T.List["Step"] = []

    def __enter__(self):
        from sunya.scenarios.models.scenario import get_scenario

        get_scenario().stack.append(self)

    def __exit__(self, *args):
        from sunya.scenarios.models.scenario import get_scenario

        get_scenario().stack.pop()

    def __getattr__(self, name):
        def relates_to(other_entity=None):
            self.rel.fact_bits = (
                *self.rel.fact_bits,
                name,
                *([] if other_entity is None else [other_entity]),
            )
            return self

        return relates_to
