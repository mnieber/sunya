from dataclassy import dataclass
import typing as T
from sunya.steps.models.rel import Rel
from sunya.steps.models.step import Step


@dataclass(kw_only=True)
class Goal:
    rel: Rel
    steps: T.List[Step] = []

    def get_step(self) -> Step:
        if not self.steps:
            raise NoStepError("No steps in the current scenario.")
        return self.steps[-1]

    def get_step_or_none(self) -> Step | None:
        if not self.steps:
            return None
        return self.get_step()


class NoStepError(Exception):
    pass
