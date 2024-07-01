from django.db import models

from common.models import BaseModel


class Organization(BaseModel):
    name = models.TextField()
