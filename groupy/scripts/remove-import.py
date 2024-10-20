import sys
from typing import Union

import libcst as cst


class ImportRemover(cst.CSTTransformer):
    def __init__(self, import_to_remove: str):
        self.import_to_remove = import_to_remove

    def leave_Import(
        self, original_node: cst.Import, updated_node: cst.Import
    ) -> Union[cst.Import, cst.RemovalSentinel]:
        __import__("pudb").set_trace()  # zz
        new_names = [
            alias
            for alias in updated_node.names
            if alias.name.value != self.import_to_remove
        ]
        if not new_names:
            return cst.RemoveFromParent()
        return updated_node.with_changes(names=new_names)

    def leave_ImportFrom(
        self, original_node: cst.ImportFrom, updated_node: cst.ImportFrom
    ) -> Union[cst.ImportFrom, cst.RemovalSentinel]:
        __import__("pudb").set_trace()  # zz
        if updated_node.module:
            if isinstance(updated_node.module, cst.Name):
                module = updated_node.module.value
            elif isinstance(updated_node.module, cst.Attribute):
                module = self.get_full_attribute_name(updated_node.module)
            else:
                module = ""  # Unexpected type, treat as if no module specified
        else:
            module = ""

        if module == self.import_to_remove:
            return cst.RemoveFromParent()

        new_names = [
            alias
            for alias in updated_node.names
            if f"{module}.{alias.name.value}" != self.import_to_remove
        ]
        if not new_names:
            return cst.RemoveFromParent()
        return updated_node.with_changes(names=new_names)

    def get_full_attribute_name(self, attr: cst.Attribute) -> str:
        if isinstance(attr.value, cst.Name):
            return f"{attr.value.value}.{attr.attr.value}"
        elif isinstance(attr.value, cst.Attribute):
            return f"{self.get_full_attribute_name(attr.value)}.{attr.attr.value}"
        else:
            return attr.attr.value  # Unexpected case, return just the attribute name


def remove_import(filename: str, import_to_remove: str):
    # Read the file
    with open(filename, "r") as file:
        source_code = file.read()

    # Parse the source code
    source_tree = cst.parse_module(source_code)

    # Remove the specified import
    transformer = ImportRemover(import_to_remove)
    modified_tree = source_tree.visit(transformer)

    # Write the modified code back to the file
    with open(filename, "w") as file:
        file.write(modified_tree.code)

    print(f"Removed import '{import_to_remove}' from {filename}")


if __name__ == "__main__":
    __import__("pudb").set_trace()  # zz
    if len(sys.argv) != 3:
        print("Usage: python script.py <filename> <import_to_remove>")
        sys.exit(1)

    filename, import_to_remove = sys.argv[1], sys.argv[2]
    remove_import(filename, import_to_remove)
