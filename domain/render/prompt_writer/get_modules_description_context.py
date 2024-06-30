from mock.datatypes import Module
from sunya.utils.case import camel_to_snake, l0
from sunya.utils.inspect import find_root_class, get_class_source


def get_modules_description_context(entities, module_order):
    modules = _get_modules(entities, module_order)
    context = dict(modules=[])
    for module in module_order:
        if module not in modules:
            continue

        context["modules"].append(
            dict(
                name=l0(camel_to_snake(module.__name__)),
                source_code=get_class_source(module),
                api_views=_get_api_views(module),
            )
        )
    return context


def _get_modules(entities, module_order):
    modules = set()
    for entity in entities:
        if root_class := find_root_class(entity.__class__, Module):
            if root_class not in module_order:
                raise ValueError(f"Module {root_class} is not in the module order")
            modules.add(root_class)
    return modules


def _get_api_views(module):
    result = []
    if api_views := getattr(module, "ApiViews", None):
        for name, member in vars(api_views).items():
            if isinstance(member, type):  # Check if the member is a class
                result.append(dict(name=name))
    return result
