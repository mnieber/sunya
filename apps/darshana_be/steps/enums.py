from django.db import models


class FactBitTypeNames(models.TextChoices):
    STRING = "string"
    ROLE = "role"
    ACTOR = "actor"


class StepTypeNames(models.TextChoices):
    STEP = "step"
    GOAL = "goal"
    ROOT = "root"
