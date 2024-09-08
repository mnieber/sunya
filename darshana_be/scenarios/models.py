from django.db import models
from common.models import BaseModel
from common.fields import SingleLineTextField
from steps.models import Step
from projects.models import Project


class Scenario(BaseModel):
    name = SingleLineTextField()
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="scenarios"
    )
    root_step = models.OneToOneField(Step, on_delete=models.CASCADE, related_name="+")

    def __str__(self):
        return self.name
