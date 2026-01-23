import json
import hashlib
import pytest
from django.contrib.gis.geos import GEOSGeometry

from polygons.actions.create_polygon import (
    create_polygon,
    CreatePolygonForm,
    InvalidPolygonGeometryError,
)


class TestCreatePolygonAction:
    @pytest.mark.django_db
    def test_create_polygon_action_success(self):
        # Given
        polygon_geojson = {
            "type": "Polygon",
            "coordinates": [
                [[0.0, 0.0], [0.0, 1.0], [1.0, 1.0], [1.0, 0.0], [0.0, 0.0]]
            ],
        }
        create_polygon_form = CreatePolygonForm(polygon_geojson=polygon_geojson)

        # When
        polygon = create_polygon(create_polygon_form)

        # Then
        assert polygon.id is not None

        # Verify the geometry was correctly parsed
        geojson_str = json.dumps(polygon_geojson)
        expected_geometry = GEOSGeometry(geojson_str)
        assert polygon.polygon.equals(expected_geometry)

        # Verify the CRC is calculated correctly
        expected_crc = hashlib.md5(geojson_str.encode("utf-8")).hexdigest()
        assert polygon.crc == expected_crc

        # Verify the area is calculated correctly (1 square unit = 0.0001 hectares)
        assert polygon.area == pytest.approx(0.0001)

    @pytest.mark.django_db
    def test_create_polygon_action_invalid_geometry(self):
        # Given
        # This is a LineString, not a Polygon
        line_geojson = {"type": "LineString", "coordinates": [[0.0, 0.0], [1.0, 1.0]]}
        create_polygon_form = CreatePolygonForm(polygon_geojson=line_geojson)

        # When/Then
        with pytest.raises(InvalidPolygonGeometryError):
            create_polygon(create_polygon_form)
