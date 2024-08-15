from datetime import datetime

from landler.stack.namespace import Module, JSON, Enum
from sunya import Entity, actor_to_str


class Facts(Module):
    class Models:
        class Fact(Entity):
            name: "Facts.Enums.FactNames"
            value: JSON
            ref_date: datetime
            ref_source_id: str

    class Enums:
        class FactNames(Enum):
            CARBON_BG = "carbon_bg"
            WHC = "whc"
            TEMPERATURE = "temperature"


@actor_to_str.method((Facts.Models.Fact,))
def fact_to_str(fact):
    return f"{fact.name}+:fact"
