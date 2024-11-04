import os
from typing import Dict, List, Optional

import libcst as cst
from groupy.models import FileInfo, FunctionInfo


def analyze_file(file_path: str, package_path: str) -> FileInfo:
    with open(file_path, "r") as file:
        try:
            code = file.read()
            tree = cst.parse_module(code)

            # Calculate module path
            relative_path = os.path.relpath(file_path, package_path)
            module_path = os.path.splitext(relative_path)[0].replace(os.path.sep, ".")

            import_collector = ImportCollector()
            tree.visit(import_collector)

            # Collect functions first
            function_collector = FunctionAndConstantCollector()
            tree.visit(function_collector)

            # Pass the function_collector to FunctionCallCollector
            call_collector = FunctionCallCollector(
                imports=import_collector.imports,
                module_path=module_path,
                function_collector=function_collector,
            )
            tree.visit(call_collector)

            function_infos = [
                _create_function_info(
                    ".".join([module_path, func]), call_collector.callers.get(func, [])
                )
                for func in function_collector.functions
            ]

            return FileInfo(
                file_path=file_path,
                function_infos=function_infos,
                constants=function_collector.constants,
            )
        except Exception as e:
            print(f"Error analyzing file {file_path}: {str(e)}")
            return FileInfo(file_path=file_path, function_infos=[], constants=[])


def _create_function_info(function_path: str, callers):
    caller_paths = []
    for caller in callers:
        caller_paths.append(caller)

    return FunctionInfo(function_path=function_path, caller_paths=caller_paths)


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
    def __init__(
        self,
        imports: Dict[str, str],
        module_path: str,
        function_collector: "FunctionAndConstantCollector",
    ):
        self.imports = imports
        self.module_path = module_path
        self.function_collector = function_collector
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
            # Check if this is a local top-level function
            if node.value in self.function_collector.functions:
                return f"{self.module_path}.{node.value}"
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
