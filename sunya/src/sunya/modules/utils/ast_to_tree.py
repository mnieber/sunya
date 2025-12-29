import ast


def ast_to_tree(class_node):
    """
    Convert an AST ClassDef node to a tree structure.

    Args:
        class_node: ast.ClassDef node

    Returns:
        Dict representing the class hierarchy with metadata
    """
    if not isinstance(class_node, ast.ClassDef):
        return {}

    tree = {
        "_type": "Module",
        "_name": class_node.name,
    }

    # Extract base class name
    if class_node.bases:
        base_name = _get_name_from_node(class_node.bases[0])
        if base_name:
            tree["_base"] = base_name

    # Process class body
    for node in class_node.body:
        if isinstance(node, ast.ClassDef):
            # Nested class (e.g., Models, Actions, Forms)
            tree[node.name] = _process_nested_class(node)
        elif isinstance(node, ast.AnnAssign):
            # Annotated field at top level (rare but possible)
            field_info = _process_field(node)
            if field_info:
                tree[field_info["name"]] = field_info["value"]

    return tree


def _process_nested_class(class_node):
    """Process a nested class (like Models, Actions, or specific entities)."""
    tree = {
        "_type": "Section",
        "_name": class_node.name,
    }

    # Extract base class if present
    if class_node.bases:
        base_name = _get_name_from_node(class_node.bases[0])
        if base_name:
            tree["_base"] = base_name

    # Process the class body
    for node in class_node.body:
        if isinstance(node, ast.ClassDef):
            # Further nested class (e.g., User, CreateUserForm)
            tree[node.name] = _process_entity_class(node)
        elif isinstance(node, ast.AnnAssign):
            # Field in the section
            field_info = _process_field(node)
            if field_info:
                tree[field_info["name"]] = field_info["value"]
        elif isinstance(node, ast.Pass):
            # Empty class body
            continue

    return tree


def _process_entity_class(class_node):
    """Process an entity class (like User, CreateUserForm, etc.)."""
    tree = {
        "_type": "Class",
        "_name": class_node.name,
    }

    # Extract base class
    if class_node.bases:
        base_name = _get_name_from_node(class_node.bases[0])
        if base_name:
            tree["_base"] = base_name

    # Process fields
    for node in class_node.body:
        if isinstance(node, ast.AnnAssign):
            field_info = _process_field(node)
            if field_info:
                tree[field_info["name"]] = field_info["value"]
        elif isinstance(node, ast.Assign):
            # Regular assignment (e.g., enum values without type annotations)
            assign_info = _process_assign(node)
            if assign_info:
                tree[assign_info["name"]] = assign_info["value"]
        elif isinstance(node, ast.ClassDef):
            # Nested class within entity (like Args in Actions)
            tree[node.name] = _process_entity_class(node)

    return tree


def _process_field(ann_assign_node):
    """
    Process an annotated assignment (field).

    Args:
        ann_assign_node: ast.AnnAssign node

    Returns:
        Dict with 'name' and 'value' keys, or None if invalid
    """
    if not isinstance(ann_assign_node.target, ast.Name):
        return None

    field_name = ann_assign_node.target.id
    field_value = {
        "_type": "field",
    }

    # Extract type annotation
    if ann_assign_node.annotation:
        annotation_str = _annotation_to_string(ann_assign_node.annotation)
        if annotation_str:
            field_value["_annotation"] = annotation_str

    # Extract default value if present
    if ann_assign_node.value:
        default_str = _value_to_string(ann_assign_node.value)
        if default_str:
            field_value["_default"] = default_str

    return {"name": field_name, "value": field_value}


def _process_assign(assign_node):
    """
    Process a regular assignment (without type annotation).

    This handles cases like enum values:
        CoolfarmToolCO2 = "coolfarm_tool_co2"

    Args:
        assign_node: ast.Assign node

    Returns:
        Dict with 'name' and 'value' keys, or None if invalid
    """
    # ast.Assign can have multiple targets, but for simple cases we expect one
    if len(assign_node.targets) != 1:
        return None

    target = assign_node.targets[0]
    if not isinstance(target, ast.Name):
        return None

    field_name = target.id
    field_value = {
        "_type": "field",
    }

    # Extract the assigned value
    if assign_node.value:
        default_str = _value_to_string(assign_node.value)
        if default_str:
            field_value["_default"] = default_str

    return {"name": field_name, "value": field_value}


def _get_name_from_node(node):
    """Get the name from an AST node (handles Name and Attribute nodes)."""
    if isinstance(node, ast.Name):
        return node.id
    elif isinstance(node, ast.Attribute):
        # For qualified names like typing.Optional, just return the attr
        return node.attr
    elif isinstance(node, ast.Subscript):
        # For generic types like List[str], return the base
        return _get_name_from_node(node.value)
    return None


def _annotation_to_string(annotation_node):
    """Convert an annotation AST node to a string representation."""
    return ast.unparse(annotation_node)


def _value_to_string(value_node):
    """Convert a value AST node to a string representation."""
    return ast.unparse(value_node)
