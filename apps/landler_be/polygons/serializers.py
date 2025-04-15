from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from common.serializers import BaseModelSerializer, ReadSerializerMixin
from common.form_serializer import FormSerializer
from polygons.models import Polygon
from polygons.actions.create_polygon import CreatePolygonForm


class CreatePolygonFormSerializer(FormSerializer):
    class Meta:
        form_class = CreatePolygonForm


class PolygonSerializer(ReadSerializerMixin, BaseModelSerializer):
    class Meta:
        model = Polygon
        fields = ["id", "polygon", "crc", "area"]


class PolygonGeoSerializer(GeoFeatureModelSerializer):
    """
    GeoJSON serializer for Polygon model.
    Returns polygon in standard GeoJSON format.
    """

    class Meta:
        model = Polygon
        geo_field = "polygon"
        fields = ["id", "crc", "area"]
