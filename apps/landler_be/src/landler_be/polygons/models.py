from common.models import BaseModel
from django.contrib.gis.db import models


class Polygon(BaseModel):
    polygon = models.MultiPolygonField()
    crc = models.TextField()
    area = models.FloatField(help_text="Area of the polygon in ha")

    def __str__(self):
        return f"Polygon {self.id} ({self.area:.2f} ha)"
