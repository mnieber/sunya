from django.contrib.auth import get_user_model
from django.db import models

from checklists.enums import ChecklistItemNames
from common.fields import SingleLineTextField
from common.models import BaseModel

User = get_user_model()


class Checklist(BaseModel):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="checklists")

    def __str__(self):
        return f"Checklist for {self.owner.email}"


class ChecklistItem(BaseModel):
    checklist = models.ForeignKey(
        Checklist, on_delete=models.CASCADE, related_name="items"
    )
    name = SingleLineTextField(choices=ChecklistItemNames.choices)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
