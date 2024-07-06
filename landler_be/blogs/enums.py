from django.db import models


class Audiences(models.TextChoices):
    EXPERT = "expert"
    NOVICE = "novice"
    ANY = "any"
