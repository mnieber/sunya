import typing as T

if T.TYPE_CHECKING:
    pass

from default.frontend.entities import Facet, Mutation, Query
from default.stack.namespace import Module
from sunya import EntityWithId
from sunya import G as g
from sunya import actor_to_str


class Checklist(Module):
    class Types:
        class Checklist(EntityWithId):
            items: T.List["Checklist.Types.ChecklistItem"] = []

        class ChecklistItem(EntityWithId):
            name: str
            description: str
            is_completed: bool

    class Mutations:
        class UpdateChecklistItems(Mutation):
            class Args:
                is_completed: T.Dict[str, bool]

    class Queries:
        class GetChecklist(Query):
            pass

    class States:
        class ChecklistState:
            class Containers:
                class ChecklistCtr:
                    data: Facet
                    visibility: Facet

    class StateProviders:
        class ChecklistStateProvider:
            pass

    class Views:
        class ChecklistView:
            pass

        class ChecklistItem:
            pass

    class Components:
        class ChecklistCard:
            props = dict(trim="")


g.get_checklist_query = Checklist.Queries.GetChecklist()
g.update_checklist_items_mutation = Checklist.Mutations.UpdateChecklistItems()


@actor_to_str.method((Checklist.Types.Checklist,))
def checklist_to_str(checklist):
    return f":checklist"


@actor_to_str.method((Checklist.Types.ChecklistItem,))
def checklist_item_to_str(checklist_item):
    return f"{checklist_item.name}+:checklist_item"
