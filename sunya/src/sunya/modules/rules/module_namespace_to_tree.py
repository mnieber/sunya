def module_namespace_to_tree(module_namespace):
    """
    Convert a ModuleNamespace instance to a tree structure.

    Args:
        module_namespace: ModuleNamespace instance (typically M)

    Returns:
        Dict mapping module names to their tree structures
    """
    trees = {}

    # Access the internal _modules dict
    if not hasattr(module_namespace, "_modules"):
        return trees

    for module_name, module_spec in module_namespace._modules.items():
        trees[module_name] = _module_spec_to_tree(module_spec)

    return trees


def _module_spec_to_tree(module_spec):
    """Convert a ModuleSpec to tree structure."""
    tree = {
        "_type": "Module",
        "_name": module_spec._module_name,
        "_source": "dynamic",  # Mark as dynamically generated
    }

    # Process sections
    if hasattr(module_spec, "_sections"):
        for section_name, section_spec in module_spec._sections.items():
            tree[section_name] = _section_spec_to_tree(section_spec)

    return tree


def _section_spec_to_tree(section_spec):
    """Convert a SectionSpec to tree structure."""
    tree = {
        "_type": "Section",
        "_name": section_spec._section_name,
        "_source": "dynamic",
    }

    # Process actors
    if hasattr(section_spec, "_actors"):
        for actor_name, actor_spec in section_spec._actors.items():
            tree[actor_name] = _actor_spec_to_tree(actor_spec)

    return tree


def _actor_spec_to_tree(actor_spec):
    """Convert an ActorSpec to tree structure."""
    return {
        "_type": "Actor",
        "_name": actor_spec._actor_name,
        "_source": "dynamic",
        "_full_path": actor_spec.full_path,
    }
