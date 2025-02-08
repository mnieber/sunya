from sunya.nodes.models.fact import get_anchor
from sunya.nodes.models.tag import Tag
from sunya.nodes.rules.it import It
from sunya.nodes.rules.the import CallsThe, The


def get_expanded_fact_bits(fact_bits, parent_node):
    tags = []
    expanded_fact_bits = []
    for fact_bit in fact_bits:
        pos = len(expanded_fact_bits)
        if isinstance(fact_bit, It):
            if not parent_node:
                raise UnmatchedItClause("It clause used without a parent node.")

            anchor = get_anchor(parent_node)
            if not anchor:
                raise UnmatchedItClause(
                    "It clause used without an anchor in the parent node."
                )

            expanded_fact_bits += anchor
            tags.append(Tag(name="It", range=(pos, pos + len(anchor))))
        elif isinstance(fact_bit, CallsThe):
            expanded_fact_bits += ("calls_the", fact_bit.entity)
            tags.append(Tag(name="CallsThe", range=(pos, pos + 2)))
        elif isinstance(fact_bit, The):
            prefix = "The" if pos == 0 else "the"
            expanded_fact_bits += (prefix, fact_bit.entity)
            tags.append(Tag(name="The", range=(pos, pos + 2)))
        else:
            expanded_fact_bits.append(fact_bit)

    return tuple(expanded_fact_bits), tags


class UnmatchedItClause(Exception):
    pass
