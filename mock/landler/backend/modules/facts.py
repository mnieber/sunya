from datetime import datetime

from landler.stack.entities import JSON, Enum, Module
from sunya import Entity, actor_to_str


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
