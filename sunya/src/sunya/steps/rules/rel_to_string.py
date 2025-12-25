from sunya.steps.rules.the import The
from sunya.actors.models.role import Role
from sunya.actors.models.entity import Entity
from sunya.steps.models.rel import Rel


def rel_to_string(rel: Rel) -> str:
    parts = [_term_to_str(x) for x in rel.fact_bits]

    return " ".join(parts)


def _term_to_str(term: any) -> str:
    from sunya.steps.rules.it import It

    if isinstance(term, str):
        return term.replace("_", " ")

    if isinstance(term, Role):
        return term.name

    if isinstance(term, The):
        return "the " + _term_to_str(term.entity)

    if isinstance(term, Rel):
        return " ".join([_term_to_str(x) for x in term.fact_bits])

    if isinstance(term, It):
        return "it"

    if isinstance(term, Entity):
        return term.__class__.__name__

    raise ValueError(f"Cannot convert term of type {type(term)} to string.")
