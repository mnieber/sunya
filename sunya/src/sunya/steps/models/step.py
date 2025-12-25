from dataclassy import dataclass
from sunya.steps.models.rel import Rel


@dataclass(kw_only=True)
class Step:
    rel: Rel
