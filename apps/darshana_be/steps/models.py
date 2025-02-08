from common.fields import SingleLineTextField
from django.db import models
from common.models import BaseModel
from dataclassy import dataclass
from steps.enums import StepTypeNames


@dataclass
class FactBit:
    type_name: str
    value: str


class Step(BaseModel):
    type_name = SingleLineTextField(choices=StepTypeNames.choices)
    fact_json = models.JSONField()
    parent_step = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="child_steps",
    )
    field_delta_set_by_actor_key = models.JSONField(default=dict)
    pre_actor_key_by_role_name = models.JSONField(default=dict)
    post_actor_key_by_role_name = models.JSONField(default=dict)
    scenario = models.ForeignKey(
        "scenarios.Scenario", on_delete=models.CASCADE, related_name="steps"
    )

    def __str__(self):
        return f"Step {" ".join([fb.value for fb in self.fact])}"

    @property
    def fact(self):
        return [FactBit(**fb) for fb in self.fact_json]
