def component_namespace_to_tree(component_namespace):
    """
    Convert a ComponentNamespace instance to a tree structure.

    Args:
        component_namespace: ComponentNamespace instance (typically C)

    Returns:
        Dict mapping module names to their tree structures
    """
    trees = {}

    # Access the internal _component dict
    if not hasattr(component_namespace, "_component"):
        return trees

    for component_name, component_spec in component_namespace._component.items():
        trees[component_name] = _component_spec_to_tree(component_spec)

    return trees


def _component_spec_to_tree(component_spec):
    """Convert a ComponentSpec to tree structure."""
    tree = {
        "_type": "Component",
        "_name": component_spec._component_name,
        "_source": "dynamic",  # Mark as dynamically generated
    }

    # Process modules
    if hasattr(component_spec, "_modules"):
        for module_name, module_spec in component_spec._modules.items():
            tree[module_name] = _module_spec_to_tree(module_spec)

    return tree


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
