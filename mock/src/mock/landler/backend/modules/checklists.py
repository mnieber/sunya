from mock.django_app.namespace import Action, ApiView, DjangoModule
from mock.landler.backend.modules.users import Users
from sunya import Entity, RelatedSet, FK


class Checklists(DjangoModule):
    class Models:
        class Checklist(Entity):
            _owner: "Users.Models.User"
            items: RelatedSet["Checklists.Models.ChecklistItem"] = []

        class ChecklistItem(Entity):
            name: str
            is_completed: bool = False
            checklist: FK["Checklists.Models.Checklist"]

    class Actions:
        class GetOrCreateChecklist(Action):
            class Args:
                user: "Users.Models.User"

        class UpdateChecklistItem(Action):
            class Args:
                checklist_item: "Checklists.Models.ChecklistItem"
                is_completed: bool

    class Api:
        class GetChecklist(ApiView):
            pass

        class UpdateChecklistItem(ApiView):
            pass

    class DomainEvents:
        class ChecklistCreated:
            pass

        class ChecklistItemUpdated:
            pass
