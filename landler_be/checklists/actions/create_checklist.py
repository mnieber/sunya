from checklists.models import Checklist, ChecklistItem
from django.contrib.auth import get_user_model
from checklists.enums import ChecklistItemNames

User = get_user_model()


User = get_user_model()


def create_checklist(user) -> Checklist:
    checklist = Checklist.objects.create(owner=user)

    # Create default checklist items
    for item in ChecklistItemNames.values:
        ChecklistItem.objects.create(
            checklist=checklist,
            title=item,
            is_completed=False,
        )

    return checklist
