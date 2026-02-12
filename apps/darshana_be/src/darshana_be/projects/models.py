from django.db import models
from darshana_be.common.fields import SingleLineTextField
from darshana_be.common.models import BaseModel


class Project(BaseModel):
    name = SingleLineTextField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
