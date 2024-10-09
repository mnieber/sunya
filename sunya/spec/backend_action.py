from sunya.utils import extract_field_types


def backend_action(action_class):
    result = dict(name=action_class.__name__)
    args = getattr(action_class, "Args", None) or []
    if args:
        result["args"] = [
            dict(name=name, type=cls) for name, cls in extract_field_types(args).items()
        ]
    return result
