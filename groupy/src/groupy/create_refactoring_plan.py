from groupy.models import FileRefactoringPlan
from groupy.models.file_info import FileInfo


def create_refactoring_plan(file_tree):
    tree_structure = {}

    for filename, node in file_tree.items():
        if isinstance(node, FileInfo):
            __import__("pudb").set_trace()  # zz
            tree_structure[filename] = _create_refactoring_plan(node)
        else:
            tree_structure[filename] = create_refactoring_plan(node)

    return tree_structure


def _create_refactoring_plan(file_info):
    return FileRefactoringPlan()
