from dataclassy import dataclass
from typing import Dict, Any

from polygons.models import Polygon
from django.contrib.gis.geos import GEOSGeometry, MultiPolygon as GEOSMultiPolygon
import hashlib
import json


@dataclass
class CreatePolygonForm:
    polygon_geojson: Dict[str, Any]


def create_polygon(create_polygon_form: CreatePolygonForm) -> Polygon:
    # Validate the GeoJSON is a proper polygon
    polygon_geojson = create_polygon_form.polygon_geojson

    # Convert GeoJSON to GeoDjango polygon
    geojson_str = json.dumps(polygon_geojson, sort_keys=True)
    geometry = GEOSGeometry(geojson_str)

    # Check if it's actually a polygon
    if geometry.geom_type.upper() not in ["POLYGON", "MULTIPOLYGON"]:
        raise InvalidPolygonGeometryError(
            f"Expected POLYGON or MULTIPOLYGON, got {geometry.geom_type}"
        )

    # Calculate CRC for being able to avoid duplicate polygons
    crc = hashlib.md5(geojson_str.encode("utf-8")).hexdigest()

    # Convert single Polygon to MultiPolygon for consistent storage
    if geometry.geom_type == "Polygon":
        geometry = GEOSMultiPolygon(geometry)

    # Calculate area in hectares
    area_ha = _calculate_area_hectares(geometry)

    # Create the polygon
    polygon = Polygon(polygon=geometry, crc=crc, area=area_ha)
    polygon.save()

    return polygon


def _calculate_area_hectares(geometry: GEOSGeometry) -> float:
    """Calculate area in hectares using a projected CRS.

    For geometries in WGS84 (EPSG:4326), .area returns square degrees
    which is not useful. We transform to World Mercator (EPSG:3395)
    to get area in square meters, then convert to hectares.
    """
    # Transform to World Mercator (EPSG:3395) for area calculation
    geometry_projected = geometry.transform(3395, clone=True)
    # Area in square meters, convert to hectares (1 ha = 10000 m²)
    return geometry_projected.area / 10000


class InvalidPolygonGeometryError(Exception):
    """Raised when the provided GeoJSON doesn't represent a valid polygon geometry"""
