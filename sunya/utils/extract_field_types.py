from typing import get_args, get_origin


def get_type_name(type_annotation):
    # Handle built-in types
    if type_annotation in (str, int, float, bool, list, dict, tuple, set):
        return type_annotation.__name__

    # Handle typing generics
    origin = get_origin(type_annotation)
    if origin is not None:
        args = get_args(type_annotation)
        if origin in (list, dict, tuple, set):
            if args:
                return f"{origin.__name__}[{', '.join(get_type_name(arg) for arg in args)}]"
            return origin.__name__

    # Convert the type annotation to a string
    type_str = str(type_annotation)

    # Extract the last term of the type expression
    type_name = type_str.split(".")[-1]

    # remove everying after the last quote
    if "'" in type_name:
        type_name = type_name[: type_name.rindex("'")]

    return type_name


def extract_field_types(cls):
    field_types = {}
    if hasattr(cls, "id"):
        field_types["id"] = "UUID"

    # Get the class annotations
    annotations = cls.__annotations__ if hasattr(cls, "__annotations__") else {}

    for field_name, type_annotation in annotations.items():
        if field_name.startswith("_"):
            continue

        field_type = get_type_name(type_annotation)
        if attr := getattr(cls, field_name, None):
            field_type += f" = {attr}"
        field_types[field_name] = field_type

    return field_types
