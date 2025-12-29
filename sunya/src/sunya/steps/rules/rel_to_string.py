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
        term_str = term.replace("_", " ")

    elif isinstance(term, Role):
        term_str = term.name

    elif isinstance(term, The):
        term_str = "the " + _term_to_str(term.entity)

    elif isinstance(term, Rel):
        term_str = " ".join([_term_to_str(x) for x in term.fact_bits])

    elif isinstance(term, It):
        term_str = "it"

    elif isinstance(term, Entity):
        term_str = term.__class__.__name__

    else:
        raise ValueError(f"Cannot convert term of type {type(term)} to string.")

    return term_str.strip("_")
