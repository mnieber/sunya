import typing as T

if T.TYPE_CHECKING:
    pass

from landler.frontend.entities import Mutation, Facet, Trim, Route, Query
from landler.stack.entities import Module
from sunya import EntityWithId, actor_to_str


class Checklist(Module):
    class Types:
        class ChecklistItem(EntityWithId):
            title: str
            description: str
            is_completed: bool
            is_minimized: bool

    class Mutations:
        class UpdateChecklistItems(Mutation):
            class Args:
                is_minimized: T.Dict[str, bool]
                is_hidden: T.Dict[str, bool]

    class Queries:
        class GetChecklist(Query):
            pass

    class States:
        class ChecklistState:
            class Containers:
                class ChecklistCtr:
                    data: Facet
                    visibility: Facet

    class Routes:
        class HomePageRoute(Route):
            pass

    class StateProviders:
        class ChecklistStateProvider:
            pass

    class Views:
        class ChecklistView:
            pass

    class Components:
        class ChecklistCard:
            trim: Trim


get_checklist_query = Checklist.Queries.GetChecklist()
update_checklist_items_mutation = Checklist.Mutations.UpdateChecklistItems()
home_page_route = Checklist.Routes.HomePageRoute(path="/home")


@actor_to_str.method((Checklist.Types.ChecklistItem,))
def checklist_item_to_str(checklist_item):
    return f"{checklist_item.title}+:checklist_item"
