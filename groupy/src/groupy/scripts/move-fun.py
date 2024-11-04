import os
import sys
from typing import Optional

import libcst as cst


class FunctionCollector(cst.CSTVisitor):
    def __init__(self, function_name: str):
        self.function_name = function_name
        self.function_node: Optional[cst.FunctionDef] = None

    def visit_FunctionDef(self, node: cst.FunctionDef) -> Optional[bool]:
        if node.name.value == self.function_name:
            self.function_node = node
            return False
        return True


class FunctionRemover(cst.CSTTransformer):
    def __init__(self, function_name: str):
        self.function_name = function_name

    def leave_Module(
        self, original_node: cst.Module, updated_node: cst.Module
    ) -> cst.Module:
        new_body = [
            stmt
            for stmt in updated_node.body
            if not (
                isinstance(stmt, cst.FunctionDef)
                and stmt.name.value == self.function_name
            )
        ]
        return updated_node.with_changes(body=new_body)


def move_function(source_file: str, function_name: str, target_file: str):
    # Read source file
    with open(source_file, "r") as f:
        source_code = f.read()

    # Parse the source code
    source_tree = cst.parse_module(source_code)

    # Collect the function
    collector = FunctionCollector(function_name)
    source_tree.visit(collector)

    if collector.function_node is None:
        print(f"Function '{function_name}' not found in {source_file}")
        return

    # Remove the function from the source file
    remover = FunctionRemover(function_name)
    modified_source = source_tree.visit(remover)

    # Write the modified source back to the file
    with open(source_file, "w") as f:
        f.write(modified_source.code)

    # Read target file
    if os.path.exists(target_file):
        with open(target_file, "r") as f:
            target_code = f.read()
    else:
        target_code = ""
    target_tree = cst.parse_module(target_code)

    # Add the function to the target file
    new_body = list(target_tree.body) + [collector.function_node]
    modified_target = target_tree.with_changes(body=new_body)

    # Write the modified target
    with open(target_file, "w") as f:
        f.write(modified_target.code)

    print(
        f"Function '{function_name}' successfully moved from {source_file} to {target_file}"
    )


if __name__ == "__main__":
    __import__("pudb").set_trace()  # zz
    if len(sys.argv) != 4:
        print("Usage: python script.py <source_file> <function_name> <target_file>")
        sys.exit(1)

    source_file, function_name, target_file = sys.argv[1], sys.argv[2], sys.argv[3]
    move_function(source_file, function_name, target_file)
