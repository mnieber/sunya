from groupy.models import FileRefactoringPlan
from groupy.models.file_info import FileInfo, FunctionInfo
from groupy.models.file_refactoring_plan import FunctionRefactoringPlan


def create_refactoring_plan(file_tree):
    tree_structure = {}

    for filename, node in file_tree.items():
        if isinstance(node, FileInfo):
            tree_structure[filename] = _create_file_refactoring_plan(node)
        else:
            tree_structure[filename] = create_refactoring_plan(node)

    return tree_structure


def _create_file_refactoring_plan(file_info: FileInfo):
    file_refactoring_plan = FileRefactoringPlan()
    for function_info in file_info.function_infos:
        file_refactoring_plan.function_refactoring_plans.append(
            _create_function_refactoring_plan(function_info)
        )
    return file_refactoring_plan


def _create_function_refactoring_plan(function_info: FunctionInfo):
    return FunctionRefactoringPlan(function_path=function_info.function_path)
