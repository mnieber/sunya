from checklists.enums import ChecklistItemNames
from checklists.models import ChecklistItem


def update_checklist_item(
    user, checklist_item_name: ChecklistItemNames, is_completed: bool
) -> ChecklistItem:
    checklist_item = ChecklistItem.objects.get(
        checklist__owner=user, name=checklist_item_name
    )
    checklist_item.is_completed = is_completed
    checklist_item.save()
    return checklist_item
