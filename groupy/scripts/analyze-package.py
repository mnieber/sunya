import json
import os
from typing import Dict, List, Optional, Tuple, Union

import libcst as cst


class ImportCollector(cst.CSTVisitor):
    def __init__(self):
        self.imports: Dict[str, str] = {}

    def visit_Import(self, node: cst.Import) -> None:
        for alias in node.names:
            self.imports[
                alias.asname.name.value if alias.asname else alias.name.value
            ] = alias.name.value

    def visit_ImportFrom(self, node: cst.ImportFrom) -> None:
        if node.module is None:
            module = ""
        elif isinstance(node.module, cst.Name):
            module = node.module.value
        elif isinstance(node.module, cst.Attribute):
            module = self.get_full_name(node.module)
        else:
            module = ""  # Unexpected type, treat as if no module specified

        for alias in node.names:
            name = alias.name.value
            asname = alias.asname.name.value if alias.asname else name
            self.imports[asname] = f"{module}.{name}" if module else name

    def get_full_name(self, node: cst.CSTNode) -> str:
        if isinstance(node, cst.Name):
            return node.value
        elif isinstance(node, cst.Attribute):
            return f"{self.get_full_name(node.value)}.{node.attr.value}"
        return ""


class FunctionCallCollector(cst.CSTVisitor):
    def __init__(self, imports: Dict[str, str]):
        self.imports = imports
        self.callers: Dict[str, List[str]] = {}
        self.current_function: Optional[str] = None
        self.current_class: Optional[str] = None

    def visit_ClassDef(self, node: cst.ClassDef) -> None:
        self.current_class = node.name.value

    def leave_ClassDef(self, original_node: cst.ClassDef) -> None:
        self.current_class = None

    def visit_FunctionDef(self, node: cst.FunctionDef) -> None:
        if self.current_class:
            self.current_function = f"{self.current_class}.{node.name.value}"
        else:
            self.current_function = node.name.value

    def leave_FunctionDef(self, original_node: cst.FunctionDef) -> None:
        self.current_function = None

    def visit_Call(self, node: cst.Call) -> None:
        if self.current_function:
            called_func = self.get_called_function_name(node.func)
            if called_func:
                self.callers.setdefault(called_func, []).append(self.current_function)

    def get_called_function_name(self, node: cst.CSTNode) -> Optional[str]:
        if isinstance(node, cst.Name):
            return self.imports.get(node.value, node.value)
        elif isinstance(node, cst.Attribute):
            module = self.get_full_name(node.value)
            if module in self.imports:
                module = self.imports[module]
            return f"{module}.{node.attr.value}"
        return None

    def get_full_name(self, node: cst.CSTNode) -> str:
        if isinstance(node, cst.Name):
            return node.value
        elif isinstance(node, cst.Attribute):
            return f"{self.get_full_name(node.value)}.{node.attr.value}"
        return ""


class FunctionAndConstantCollector(cst.CSTVisitor):
    def __init__(self):
        self.functions: List[str] = []
        self.constants: List[str] = []
        self.current_class: Optional[str] = None

    def visit_ClassDef(self, node: cst.ClassDef) -> None:
        self.current_class = node.name.value

    def leave_ClassDef(self, original_node: cst.ClassDef) -> None:
        self.current_class = None

    def visit_FunctionDef(self, node: cst.FunctionDef) -> None:
        if not self.current_class:  # Only collect top-level functions
            self.functions.append(node.name.value)

    def visit_Assign(self, node: cst.Assign) -> None:
        for target in node.targets:
            if isinstance(target.target, cst.Name) and target.target.value.isupper():
                self.constants.append(target.target.value)


def analyze_file(
    file_path: str, package_path: str
) -> Dict[str, Union[List[str], List[Tuple[str, List[str]]]]]:
    with open(file_path, "r") as file:
        try:
            code = file.read()
            tree = cst.parse_module(code)

            import_collector = ImportCollector()
            tree.visit(import_collector)

            call_collector = FunctionCallCollector(import_collector.imports)
            tree.visit(call_collector)

            collector = FunctionAndConstantCollector()
            tree.visit(collector)

            relative_path = os.path.relpath(file_path, package_path)
            module_path = os.path.splitext(relative_path)[0].replace(os.path.sep, ".")

            functions_with_callers = [
                (
                    func,
                    [
                        f"{module_path}.{caller}" if "." not in caller else caller
                        for caller in call_collector.callers.get(func, [])
                    ],
                )
                for func in collector.functions
            ]

            return {
                "functions": functions_with_callers,
                "constants": collector.constants,
            }
        except Exception as e:
            print(f"Error analyzing file {file_path}: {str(e)}")
            return {"functions": [], "constants": []}


def scan_package(package_path: str) -> Dict[str, Dict[str, Union[Dict, List]]]:
    tree_structure = {}

    for root, dirs, files in os.walk(package_path):
        if os.path.basename(root).startswith("__") or os.path.basename(root).startswith(
            "."
        ):
            continue

        relative_path = os.path.relpath(root, package_path)
        current_level = tree_structure

        if relative_path != ".":
            for part in relative_path.split(os.sep):
                if part not in current_level:
                    current_level[part] = {}
                current_level = current_level[part]

        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                analysis = analyze_file(file_path, package_path)
                current_level[file] = analysis

    return tree_structure


def main(package_path: str):
    tree_structure = scan_package(package_path)
    print(json.dumps(tree_structure, indent=2))


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python script.py <package_path>")
        sys.exit(1)

    package_path = sys.argv[1]
    main(package_path)
