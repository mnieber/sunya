import typing as T

from default.backend.namespace import Action, ApiView
from default.stack.namespace import Module
from landler.backend.modules.users import Users
from sunya import EntityWithId
from sunya import G as g
from sunya import actor_to_str


class Checklists(Module):
    class Models:
        class Checklist(EntityWithId):
            items: T.List["Checklists.Models.ChecklistItem"]
            owner: "Users.Models.User"

        class ChecklistItem(EntityWithId):
            name: str
            is_completed: bool = False

    class Actions:
        class GetOrCreateChecklist(Action):
            class Args:
                user: "Users.Models.User"

        class UpdateChecklistItem(Action):
            class Args:
                checklist_item: "Checklists.Models.ChecklistItem"
                is_completed: bool

    class ApiViews:
        class GetChecklist(ApiView):
            pass

        class UpdateChecklistItem(ApiView):
            pass

    class DomainEvents:
        class ChecklistCreated:
            pass

        class ChecklistItemUpdated:
            pass


g.get_or_create_checklist_action = Checklists.Actions.GetOrCreateChecklist()
g.update_checklist_item_action = Checklists.Actions.UpdateChecklistItem()
g.get_checklist_api_view = Checklists.ApiViews.GetChecklist()
g.update_checklist_item_api_view = Checklists.ApiViews.UpdateChecklistItem()


def get_checklist_item(name):
    return next(
        item for item in g.user_session.user.checklist.items if item.name == name
    )


@actor_to_str.method((Checklists.Models.Checklist,))
def checklist_to_str(checklist):
    return f"{checklist.owner.email}+:checklist"


@actor_to_str.method((Checklists.Models.ChecklistItem,))
def checklist_item_to_str(checklist_item):
    return f"{checklist_item.name}+:checklist-item"
