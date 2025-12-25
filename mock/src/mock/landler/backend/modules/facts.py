from datetime import datetime

from kits.python_app.impl.namespace import JSON, Enum
from sunya import Entity
from kits.django_app.impl.namespace import DjangoModule


class Facts(DjangoModule):
    class Models:
        class Fact(Entity):
            name: "Facts.Enums.FactNames"
            value: JSON
            created_at: datetime
            source_id: str

    class Enums:
        class FactNames(Enum):
            CARBON_BG = "carbon_bg"
            WHC = "whc"
            TEMPERATURE = "temperature"
