from sunya.steps.models.rel import Rel


def update_step_rel(step, verb, infix="", args=None, kwargs=None):
    fact_bits = step.rel.fact_bits
    kwarg_items = [f"{k}={v}" for k, v in (kwargs or {}).items()]
    step.rel = Rel(
        fact_bits=(
            fact_bits[0],
            verb,
            fact_bits[1],
            *([infix] if infix else []),
            *(args or ()),
            *kwarg_items,
        )
    )
