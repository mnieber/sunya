from sunya.utils import camel_to_snake


def backend_api_view(api_view_class):
    return dict(name=api_view_class.__name__, filters=_get_filters(api_view_class))


def _get_filters(api_view_class):
    result = []
    filters = getattr(api_view_class, "Filters", None) or []
    for filter_name in filters:
        result.append(
            dict(
                name=camel_to_snake(filter_name),
            )
        )
    return result
