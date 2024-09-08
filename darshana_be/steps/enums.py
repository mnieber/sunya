from django.db import models


class FactBitTypeNames(models.TextChoices):
    STRING = "string"
    ROLE = "role"
    ACTOR = "actor"
