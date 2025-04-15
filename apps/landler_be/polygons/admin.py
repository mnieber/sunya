from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin

from polygons.models import Polygon


class PolygonInline(admin.StackedInline):
    model = Polygon
    extra = 0
    can_delete = False
    show_change_link = True
    readonly_fields = ["area", "crc"]


@admin.register(Polygon)
class PolygonAdmin(GISModelAdmin):
    list_display = ["id", "area", "crc", "created_at", "modified_at"]
    search_fields = ["id", "crc"]
    readonly_fields = ["area", "crc"]

    # Display the polygon field with the OpenLayers map widget
    gis_widget_kwargs = {
        "attrs": {
            "default_zoom": 12,
            "default_lon": 0,
            "default_lat": 0,
        },
    }
