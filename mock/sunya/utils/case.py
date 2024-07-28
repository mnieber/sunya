import re

_camel1 = re.compile(r"(.)([A-Z][a-z]+)")
_camel2 = re.compile("([a-z0-9])([A-Z])")


def camel_to_snake(s):
    subbed = _camel1.sub(r"\1_\2", s)
    return _camel2.sub(r"\1_\2", subbed).lower()


def camel_to_kebab(s):
    subbed = _camel1.sub(r"\1-\2", s)
    return _camel2.sub(r"\1-\2", subbed).lower()


def get_type_name(x):
    return x.__class__.__name__


def l0(x):
    return x[0].lower() + x[1:] if x else x


def u0(x):
    return x[0].upper() + x[1:] if x else x


def type_name_to_kebab(x):
    return camel_to_kebab(get_type_name(x))
