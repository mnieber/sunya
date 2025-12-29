from pathlib import Path
from sunya.modules.rules.extract_module_classes import extract_module_classes
from sunya.modules.utils.ast_to_tree import ast_to_tree
from sunya.modules.utils.merge_trees import merge_module_trees
from sunya.modules.rules.tree_to_markdown import tree_to_markdown


def get_module_markdown(module_spec_path, dynamic_trees):
    """
    Write module specs to markdown files, merging static and dynamic specs.
    """
    # Extract all Module classes from this file
    module_classes = extract_module_classes(module_spec_path)

    if not module_classes:
        return None

    # Convert AST nodes to trees
    static_trees = {}
    for class_name, class_source, ast_node in module_classes:
        static_trees[class_name] = ast_to_tree(ast_node)

    # Merge with dynamic trees (match by module name)
    merged_trees = merge_module_trees(static_trees, dynamic_trees)

    # Generate markdown for each module class
    module_md = _generate_module_markdown(module_spec_path, merged_trees)

    return module_md


def _generate_module_markdown(module_file_path, merged_trees):
    """
    Generate markdown from merged module trees.
    """
    module_stem = Path(module_file_path).stem
    markdown_parts = []

    for class_name, tree in merged_trees.items():
        module_md = tree_to_markdown(module_stem, tree)
        markdown_parts.append(module_md)

    return "".join(markdown_parts)
