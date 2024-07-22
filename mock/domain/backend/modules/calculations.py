from domain.datatypes import Enum, Module
from sunya import Entity, actor_to_str, get_actor_key


class Calculations(Module):
    class Models:
        class Calculation(Entity):
            """
            Calculation model
            """

            name: "Calculations.Enums.CalculationNames"
            version_id: str
            required_fact_names: list[str] = []
            provided_fact_names: list[str] = []

        class CoolfarmToolCO2Calculation(Calculation):
            geomodel_version: str

    class Enums:
        class CalculationNames(Enum):
            CoolfarmToolCO2 = "coolfarm_tool_co2"


@actor_to_str.method((Calculations.Models.Calculation,))
def calculation_to_str(calculation):
    return f"{calculation.name}+:calculation"


@get_actor_key.method((Calculations.Models.Calculation,))
def get_calculation_key(calculation):
    return calculation.name
