from mock.entities.python_app.namespace import Enum
from sunya import Entity
from mock.entities.django_app.namespace import DjangoModule


class Calculations(DjangoModule):
    class Models:
        class Calculation(Entity):
            name: "Calculations.Enums.CalculationNames"
            source_id: str
            required_fact_names: list[str] = []
            provided_fact_names: list[str] = []

        class CoolfarmToolCO2Calculation(Calculation):
            geomodel_version: str

    class Enums:
        class CalculationNames(Enum):
            CoolfarmToolCO2 = "coolfarm_tool_co2"
