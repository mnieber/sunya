from kits.python_app.namespace import JSON, Form
from sunya import Entity
from kits.django_app.namespace import DjangoModule


class Polygons(DjangoModule):
    class Models:
        class Polygon(Entity):
            polygon: JSON
            crc: str
            area: float

    class Actions:
        class CreatePolygon:
            class Args:
                create_polygon_form: Form
