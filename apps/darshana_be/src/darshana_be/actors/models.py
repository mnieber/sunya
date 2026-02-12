
from darshana_be.common.fields import SingleLineTextField
from darshana_be.common.models import BaseModel


class Actor(BaseModel):
    key = SingleLineTextField()

    def __str__(self):
        return self.key


class Role(BaseModel):
    name = SingleLineTextField()

    def __str__(self):
        return self.name
