def merge_trees(static_tree, dynamic_tree):
    """
    Merge static (AST-based) and dynamic (ModuleNamespace-based) trees.

    The static tree provides the detailed structure (fields, types, etc.),
    while the dynamic tree adds actors that were declared at runtime.

    Args:
        static_tree: Dict from ast_to_tree
        dynamic_tree: Dict from module_namespace_to_tree

    Returns:
        Merged tree dict
    """
    if not isinstance(static_tree, dict) or not isinstance(dynamic_tree, dict):
        # If either is not a dict, prefer static (more detailed)
        return static_tree if static_tree else dynamic_tree

    # Start with a copy of the static tree
    merged = static_tree.copy()

    # Merge in dynamic entries
    for key, dynamic_value in dynamic_tree.items():
        if key.startswith("_"):
            # Metadata keys - prefer static, but keep dynamic markers
            if key not in merged:
                merged[key] = dynamic_value
            continue

        if key not in merged:
            # New entry from dynamic tree - add it
            merged[key] = dynamic_value
        else:
            # Both have this key - need to merge
            static_value = merged[key]
            merged[key] = _merge_values(static_value, dynamic_value)

    return merged


def _merge_values(static_value, dynamic_value):
    """
    Merge two values from static and dynamic trees.

    Args:
        static_value: Value from static tree
        dynamic_value: Value from dynamic tree

    Returns:
        Merged value
    """
    # If both are dicts, do a deep merge
    if isinstance(static_value, dict) and isinstance(dynamic_value, dict):
        # Check if they're both structured nodes (have _type)
        static_type = static_value.get("_type")
        dynamic_type = dynamic_value.get("_type")

        if static_type and dynamic_type:
            # Both are structured - recursively merge
            return merge_trees(static_value, dynamic_value)
        elif static_type:
            # Only static has structure - prefer it but add dynamic children
            result = static_value.copy()
            for key, val in dynamic_value.items():
                if key not in result and not key.startswith("_"):
                    result[key] = val
            return result
        else:
            # Neither or only dynamic has structure - do simple merge
            result = static_value.copy()
            result.update(dynamic_value)
            return result

    # For non-dict values, prefer static (it has more detail)
    return static_value


def merge_module_trees(static_modules, dynamic_modules):
    """
    Merge module-level trees.

    Args:
        static_modules: Dict mapping module names to static trees
        dynamic_modules: Dict mapping module names to dynamic trees

    Returns:
        Dict mapping module names to merged trees
    """
    merged = {}

    for module_name, static_tree in static_modules.items():
        dynamic_tree = dynamic_modules.get(module_name, {})
        merged[module_name] = merge_trees(static_tree, dynamic_tree)

    return merged
