from domain.datatypes import JSON, Module
from sunya import Entity, actor_to_str


class Polygons(Module):
    class Models:
        class Polygon(Entity):
            """A Django model that contains a polygon."""

            polygon: JSON
            crc: str
            area: float


@actor_to_str.method((Polygons.Models.Polygon,))
def polygon_to_str(polygon):
    return f"{polygon.crc}+:polygon"
