from sunya.utils import camel_to_snake, l0, get_cls_members


def get_module_description_context(module):
    result = dict(
        type="module",
        name=l0(camel_to_snake(module.__name__)),
    )
    for section_name, section in get_cls_members(module):
        yaml_section_name = camel_to_snake(section_name).lower()
        result[yaml_section_name] = get_section_description_context(section)
    return result


def get_section_description_context(section):
    result = list()
    default_create_spec = getattr(section, "_create_spec", None)
    for sub_section_name, sub_section in get_cls_members(section):
        create_spec = getattr(sub_section, "_create_spec", default_create_spec)
        if not create_spec:
            continue
        result.append(create_spec(sub_section))
    return result
