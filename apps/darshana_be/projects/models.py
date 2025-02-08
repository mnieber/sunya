from django.db import models
from common.fields import SingleLineTextField
from common.models import BaseModel


class Project(BaseModel):
    name = SingleLineTextField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
