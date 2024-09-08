from django.db import models

from common.fields import SingleLineTextField
from common.models import BaseModel


class Actor(BaseModel):
    key = SingleLineTextField()

    def __str__(self):
        return self.key
