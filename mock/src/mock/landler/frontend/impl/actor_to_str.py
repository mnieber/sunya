from sunya import actor_to_str

from ..modules.checklists import Checklists
from ..modules.users import Users


@actor_to_str.method((Checklists.Types.Checklist,))
def checklist_to_str(checklist):
    return f":checklist"


@actor_to_str.method((Checklists.Types.ChecklistItem,))
def checklist_item_to_str(checklist_item):
    return f"{checklist_item.name}+:checklist_item"


@actor_to_str.method((Users.Types.User,))
def user_to_str(user):
    return f"{user.email}+:user"
