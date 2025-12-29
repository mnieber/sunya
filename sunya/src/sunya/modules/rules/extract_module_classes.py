import ast
from pathlib import Path


def extract_module_classes(filepath):
    """
    Extract all top-level classes that inherit from Module (or its subclasses).

    Returns:
        List of tuples: [(class_name, class_source_code, ast_node), ...]
    """
    filepath = Path(filepath)
    source_code = filepath.read_text()

    # Parse the source code
    try:
        tree = ast.parse(source_code)
    except SyntaxError:
        return []

    # Read the source lines for extraction
    source_lines = source_code.splitlines()

    module_classes = []

    for node in ast.walk(tree):
        # Only look at top-level ClassDef nodes
        if not isinstance(node, ast.ClassDef):
            continue

        # Check if the class has any base classes
        if not node.bases:
            continue

        # Check if any base class name contains "Module"
        # This handles: Module, DjangoModule, etc.
        for base in node.bases:
            base_name = _get_name_from_node(base)
            if base_name and base_name.endswith("Module"):
                # Extract the class source code
                class_source = _extract_class_source(node, source_lines)
                if class_source:
                    module_classes.append((node.name, class_source, node))
                break

    return module_classes


def _get_name_from_node(node):
    """Get the name from an AST node (handles Name and Attribute nodes)."""
    if isinstance(node, ast.Name):
        return node.id
    elif isinstance(node, ast.Attribute):
        return node.attr
    return None


def _extract_class_source(class_node, source_lines):
    """
    Extract the source code for a class definition.

    Args:
        class_node: AST ClassDef node
        source_lines: List of source code lines

    Returns:
        String containing the class source code
    """
    if not hasattr(class_node, "lineno") or not hasattr(class_node, "end_lineno"):
        return None

    # AST line numbers are 1-indexed
    start_line = class_node.lineno - 1
    end_line = class_node.end_lineno

    # Extract the lines
    class_lines = source_lines[start_line:end_line]

    return "\n".join(class_lines)
