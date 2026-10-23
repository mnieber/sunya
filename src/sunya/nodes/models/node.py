import typing as T

from dataclassy import dataclass
from sunya.scenarios.models.goal import Goal


@dataclass(kw_only=True)
class Node:
    goals: T.List[Goal] = []

    def get_goal(self) -> Goal:
        if not self.goals:
            raise NoGoalError("No goals in the current scenario.")
        return self.goals[-1]

    def get_goal_or_none(self) -> Goal | None:
        if not self.goals:
            return None
        return self.get_goal()


class NoGoalError(Exception):
    pass
