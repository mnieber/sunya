def tree_to_markdown(module_name, tree):
    """
    Convert a tree structure to markdown with Python code blocks.

    Args:
        module_name: Name of the module (e.g., "users")
        tree: Tree dict from ast_to_tree or merged tree

    Returns:
        Markdown string
    """
    markdown = f"# Module: {module_name}\n\n"

    # Get the module class name from the tree
    class_name = tree.get("_name", module_name.title())
    base_class = tree.get("_base", "Module")

    # Generate Python code
    python_code = _render_class(class_name, base_class, tree, indent=0)

    markdown += f"## {class_name}\n\n"
    markdown += f"```python\n{python_code}\n```\n\n"

    return markdown


def _render_class(class_name, base_class, tree, indent=0):
    """
    Render a class definition with its contents.

    Args:
        class_name: Name of the class
        base_class: Base class name (or None)
        tree: Tree dict
        indent: Current indentation level

    Returns:
        Python code string
    """
    indent_str = "    " * indent
    lines = []

    # Class declaration
    if base_class:
        lines.append(f"{indent_str}class {class_name}({base_class}):")
    else:
        lines.append(f"{indent_str}class {class_name}:")

    # Track if we've added any content
    has_content = False

    # Process children (skip metadata keys starting with _)
    children = [
        (k, v) for k, v in tree.items() if k == "__doc__" or not k.startswith("_")
    ]

    # Sort children: sections first, then fields
    sections = [
        (k, v)
        for k, v in children
        if isinstance(v, dict) and v.get("_type") in ["Section", "Class", "Module"]
    ]
    fields = [
        (k, v) for k, v in children if isinstance(v, dict) and v.get("_type") == "field"
    ]
    actors = [
        (k, v) for k, v in children if isinstance(v, dict) and v.get("_type") == "Actor"
    ]

    # Render fields first
    for field_name, field_info in fields:
        has_content = True
        field_line = _render_field(field_name, field_info, indent + 1)
        lines.append(field_line)

    # Render nested classes/sections
    for idx, (child_name, child_tree) in enumerate(sections):
        if idx > 0:
            lines.append("")

        has_content = True
        child_base = child_tree.get("_base")
        child_code = _render_class(child_name, child_base, child_tree, indent + 1)
        lines.append(child_code)

    # Render dynamic actors (those without detailed structure)
    for idx, (actor_name, actor_info) in enumerate(actors):
        if idx > 0:
            lines.append("")

        has_content = True
        actor_line = _render_actor(actor_name, actor_info, indent + 1)
        lines.append(actor_line)

    # If no content, add pass
    if not has_content:
        lines.append(f"{indent_str}    pass")

    return "\n".join(lines)


def _render_field(field_name, field_info, indent):
    """
    Render a field definition.

    Args:
        field_name: Name of the field
        field_info: Field dict with _annotation, _default
        indent: Indentation level

    Returns:
        Python code line
    """
    indent_str = "    " * indent
    annotation = field_info.get("_annotation", "Any")
    default = field_info.get("_default")

    if default is not None:
        return f"{indent_str}{field_name}: {annotation} = {default}"
    else:
        return f"{indent_str}{field_name}: {annotation}"


def _render_actor(actor_name, actor_info, indent):
    """
    Render a dynamic actor as a simple class with pass.

    Args:
        actor_name: Name of the actor
        actor_info: Actor dict
        indent: Indentation level

    Returns:
        Python code lines
    """
    indent_str = "    " * indent
    lines = [
        f"{indent_str}class {actor_name}:",
        f"{indent_str}    pass",
    ]
    return "\n".join(lines)
