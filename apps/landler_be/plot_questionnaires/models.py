from common.models import BaseModel
from django.contrib.gis.db import models


class PlotQuestionnaire(BaseModel):
    values = models.JSONField()
    crc = models.CharField(max_length=32)

    def __str__(self):
        return f"PlotQuestionnaire {self.id}"
