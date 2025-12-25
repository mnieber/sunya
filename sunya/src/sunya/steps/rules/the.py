import typing as T


def the(entity):
    from sunya.steps.models.rel import Rel

    rel_builder = Rel(fact_bits=(The(entity),))
    return T.cast(T.Any, rel_builder)


class The:
    def __init__(self, entity):
        self.entity = entity
