from sunya import extract_field_types, camel_to_snake, l0


def get_module_description_context(module):
    return dict(
        name=l0(camel_to_snake(module.__name__)),
        models=_get_models(module),
        enums=_get_enums(module),
        actions=_get_actions(module),
        api_views=_get_api_views(module),
    )


def _get_models(module):
    result = []
    if models := getattr(module, "Models", None):
        for model_name, model in _get_members(models):
            result.append(
                dict(
                    name=model_name,
                    fields=[
                        dict(name=field_name, type=field_type)
                        for field_name, field_type in extract_field_types(model).items()
                    ],
                )
            )
    return result


def _get_actions(module):
    result = []
    if actions := getattr(module, "Actions", None):
        for action_name, action in _get_members(actions):
            if isinstance(action, type):
                args = getattr(action, "Args", None) or []
                result.append(
                    dict(
                        name=camel_to_snake(action_name),
                        args=[
                            dict(name=name, type=cls)
                            for name, cls in extract_field_types(args).items()
                        ],
                    )
                )
    return result


def _get_enums(module):
    result = []
    if enums := getattr(module, "Enums", None):
        for enum_name, enum in _get_members(enums):
            members = []
            for item_name, item in _get_members(enum):
                members.append(dict(name=item_name, value=item))

            result.append(dict(name=enum_name, members=members))
    return result


def _get_api_views(module):
    result = []
    if api_views := getattr(module, "ApiViews", None):
        for api_view_name, api_view in _get_members(api_views):
            if isinstance(api_view, type):
                result.append(dict(name=api_view_name, filters=_get_filters(api_view)))
    return result


def _get_members(container):
    classes = []
    for cls_name, cls in container.__dict__.items():
        if cls_name.startswith("_"):
            continue
        classes.append((cls_name, cls))
    return classes


def _get_filters(api_view):
    result = []
    filters = getattr(api_view, "Filters", None) or []
    for filter_name in filters:
        result.append(
            dict(
                name=camel_to_snake(filter_name),
            )
        )
    return result
