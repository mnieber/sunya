import typing as T


def any_dict(**kwargs):
    return T.cast(T.Any, dict(**kwargs))
