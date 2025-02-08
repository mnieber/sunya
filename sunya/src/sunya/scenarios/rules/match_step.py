from sunya.nodes.rules.get_expanded_fact_bits import (
    get_expanded_fact_bits,
    UnmatchedItClause,
)


def match_step(step, pattern):
    try:
        expanded_pattern, _ = get_expanded_fact_bits(tuple(pattern), step.parent)
    except UnmatchedItClause:
        return False

    return expanded_pattern == step.fact.bits
