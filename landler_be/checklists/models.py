from django.db import models
from django.contrib.auth import get_user_model

from common.models import BaseModel
from common.fields import SingleLineTextField
from checklists.enums import ChecklistItemNames

User = get_user_model()


class Checklist(BaseModel):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="checklists")

    def __str__(self):
        return f"Checklist for {self.owner.email}"


class ChecklistItem(BaseModel):
    checklist = models.ForeignKey(
        Checklist, on_delete=models.CASCADE, related_name="items"
    )
    title = SingleLineTextField(choices=ChecklistItemNames.choices)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
