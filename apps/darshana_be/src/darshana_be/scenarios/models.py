from django.db import models
from darshana_be.common.models import BaseModel
from darshana_be.common.fields import SingleLineTextField
from darshana_be.steps.models import Step
from darshana_be.projects.models import Project


class Scenario(BaseModel):
    class Meta:
        ordering = ["order"]

    name = SingleLineTextField()
    order = models.PositiveIntegerField(default=1)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="scenarios"
    )
    root_step = models.OneToOneField(
        Step,
        on_delete=models.SET_NULL,
        related_name="root_scenario",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name
