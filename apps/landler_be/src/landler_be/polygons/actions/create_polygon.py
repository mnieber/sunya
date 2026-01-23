from dataclassy import dataclass
from typing import Dict, Any

from polygons.models import Polygon
from django.contrib.gis.geos import GEOSGeometry
import hashlib
import json
from units.utils.unit_conversions import m2_to_ha


@dataclass
class CreatePolygonForm:
    polygon_geojson: Dict[str, Any]


def create_polygon(create_polygon_form: CreatePolygonForm) -> Polygon:
    # Validate the GeoJSON is a proper polygon
    polygon_geojson = create_polygon_form.polygon_geojson

    # Convert GeoJSON to GeoDjango polygon
    geojson_str = json.dumps(polygon_geojson)
    geometry = GEOSGeometry(geojson_str)

    # Check if it's actually a polygon
    if not geometry.geom_type.upper() in ["POLYGON", "MULTIPOLYGON"]:
        raise InvalidPolygonGeometryError(
            f"Expected POLYGON or MULTIPOLYGON, got {geometry.geom_type}"
        )

    # Calculate CRC for being able to avoid duplicate polygons
    crc = hashlib.md5(geojson_str.encode("utf-8")).hexdigest()

    # Calculate area in hectares (convert from square meters)
    area_ha = m2_to_ha(geometry.area)

    # Create the polygon
    polygon = Polygon(polygon=geometry, crc=crc, area=area_ha)
    polygon.save()

    return polygon


class InvalidPolygonGeometryError(Exception):
    """Raised when the provided GeoJSON doesn't represent a valid polygon geometry"""
