from sunya.scenarios.actions.step_builder import StepBuilder


class It:
    def __repr__(self):
        return "It"


def it():
    return StepBuilder(fact_bits=(It(),))
