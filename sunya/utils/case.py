import re

_underscorer1 = re.compile(r"(.)([A-Z][a-z]+)")
_underscorer2 = re.compile("([a-z0-9])([A-Z])")


def camel_to_snake(s):
    subbed = _underscorer1.sub(r"\1_\2", s)
    return _underscorer2.sub(r"\1_\2", subbed).lower()


def snake_name_from_instance(x):
    return l0(camel_to_snake(x.__class__.__name__))


def l0(x):
    return x[0].lower() + x[1:] if x else x


def u0(x):
    return x[0].upper() + x[1:] if x else x
