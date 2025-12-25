from sunya.steps.models.rel import Rel


class It:
    def __repr__(self):
        return "It"


def it():
    return Rel(fact_bits=(It(),))
