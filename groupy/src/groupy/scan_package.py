import os
from groupy.analyze_file import analyze_file


def scan_package(package_path: str):
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
