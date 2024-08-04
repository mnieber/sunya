import re
from sunya.utils import extract_field_types, camel_to_snake, l0


def get_module_description_context(module):
    return dict(
        name=l0(camel_to_snake(module.__name__)),
        types=_get_types(module),
        mutations=_get_mutations(module),
        queries=_get_queries(module),
        states=_get_states(module),
        routes=_get_routes(module),
        state_providers=_get_state_providers(module),
        views=_get_views(module),
        effects=_get_effects(module),
        components=_get_components(module),
    )


def _get_types(module):
    result = []
    if types := getattr(module, "Types", None):
        for type_name, type in _get_members(types):
            result.append(
                dict(
                    name=type_name,
                    fields=[
                        dict(name=field_name, type=field_type)
                        for field_name, field_type in extract_field_types(type).items()
                    ],
                )
            )
    return result


def _get_mutations(module):
    result = []
    if mutations := getattr(module, "Mutations", None):
        for mutation_name, mutation in _get_members(mutations):
            if isinstance(mutation, type):
                args = getattr(mutation, "Args", None) or []
                result.append(
                    dict(
                        name=mutation_name,
                        args=[
                            dict(name=name, type=cls)
                            for name, cls in extract_field_types(args).items()
                        ],
                    )
                )
    return result


def _get_queries(module):
    result = []
    if queries := getattr(module, "Queries", None):
        for query_name, query in _get_members(queries):
            result.append(dict(name=query_name))
    return result


def _get_states(module):
    result = []
    if states := getattr(module, "States", None):
        for state_name, state in _get_members(states):
            if isinstance(state, type):
                result.append(dict(name=state_name, containers=_get_containers(state)))
    return result


def _get_members(container):
    classes = []
    for cls_name, cls in container.__dict__.items():
        if cls_name.startswith("_"):
            continue
        classes.append((cls_name, cls))
    return classes


def _get_containers(state):
    result = []
    containers = getattr(state, "Containers", None) or []
    for container_name, container in _get_members(containers):
        result.append(dict(name=container_name, facets=_get_facets(container)))
    return result


def _get_facets(container):
    result = []
    for facet_name in extract_field_types(container).keys():
        result.append(dict(name=facet_name))
    return result


def _get_routes(module):
    result = []
    if routes := getattr(module, "Routes", None):
        for route_name, route in _get_members(routes):
            result.append(dict(name=route_name))
    return result


def _get_state_providers(module):
    result = []
    if state_providers := getattr(module, "StateProviders", None):
        for state_provider_name, state_provider in _get_members(state_providers):
            result.append(dict(name=state_provider_name))
    return result


def _get_views(module):
    if views := getattr(module, "Views", None):
        return _get_view_types(views)
    return {}


def _get_effects(module):
    result = []
    if effects := getattr(module, "Effects", None):
        for effect_name, effect in _get_members(effects):
            result.append(dict(name=effect_name))
    return result


def _get_components(module):
    result = []
    if components := getattr(module, "Components", None):
        return _get_view_types(components)
    return result


def _get_view_types(container):
    result = {}
    for member_name, member in container.__dict__.items():
        name = member.__name__ if isinstance(member, type) else member_name
        if name.startswith("_"):
            if not re.match(r"__[A-Z]", name):
                continue

        base_classes = _get_base_classes(member)
        if base_classes:
            postfix = "(" + ", ".join(base_classes) + ")"
        else:
            postfix = ""

        result[name + postfix] = (
            _get_view_types(member) if isinstance(member, type) else member
        )
    return result


def _get_base_classes(member):
    if not isinstance(member, type):
        return []
    base_classes = []
    for base_class in member.__bases__:
        if base_class.__name__ == "object":
            continue
        base_classes.append(base_class.__name__)
    return base_classes
