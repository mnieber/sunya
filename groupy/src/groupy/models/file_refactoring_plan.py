from dataclassy import dataclass
import typing as T


@dataclass
class FileRefactoringPlan:
    function_refactoring_plans: T.List["FunctionRefactoringPlan"] = []


@dataclass
class FunctionRefactoringPlan:
    function_path: str
    move_to: str = ""
