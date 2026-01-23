import factory
from factory.django import DjangoModelFactory
from django.contrib.gis.geos import Polygon as GEOSPolygon

from polygons.models import Polygon


class PolygonFactory(DjangoModelFactory):
    """Factory for creating Polygon instances for tests."""

    # Default polygon is a simple 1x1 square
    polygon = factory.LazyFunction(
        lambda: GEOSPolygon(((0, 0), (0, 1), (1, 1), (1, 0), (0, 0)))
    )

    # CRC will be calculated automatically in the model's save method
    crc = factory.Faker("md5")

    # Area is approximately 0.0001 hectares for the default 1x1 square
    area = 0.0001

    class Meta:
        model = Polygon
