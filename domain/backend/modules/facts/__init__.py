from datetime import datetime

from mock.backend.modules.facts import Facts
from mock.datatypes import JSON, Enum, Module
from sunya import Entity, actor_to_str, get_actor_key


class Facts(Module):
    class Models:
        class Fact(Entity):
            name: "Facts.Enums.FactNames"
            value: JSON
            reference_date: datetime

    class Enums:
        class FactNames(Enum):
            CARBON_BG = "carbon_bg"
            WHC = "whc"
            TEMPERATURE = "temperature"


@actor_to_str.method((Facts.Models.Fact,))
def fact_to_str(fact):
    return f"{fact.name}+:fact"


@get_actor_key.method((Facts.Models.Fact,))
def get_fact_key(fact):
    # TODO: some id needed
    return fact.name
