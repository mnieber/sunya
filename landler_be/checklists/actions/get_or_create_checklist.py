from django.contrib.auth import get_user_model

from checklists.enums import ChecklistItemNames
from checklists.models import Checklist, ChecklistItem

User = get_user_model()


User = get_user_model()


def get_or_create_checklist(user) -> Checklist:
    if checklist := Checklist.objects.filter(owner=user).first():
        return checklist

    checklist = Checklist.objects.create(owner=user)

    # Create default checklist items
    for item in ChecklistItemNames.values:
        ChecklistItem.objects.create(
            checklist=checklist,
            name=item,
            is_completed=False,
        )

    return checklist
