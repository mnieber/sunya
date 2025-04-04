import typing as T

if T.TYPE_CHECKING:
    pass

from kits.react_app.namespace import Facet, Mutation, Query, ReactModule
from sunya import Entity, FK, RelatedSet


class Checklists(ReactModule):
    class Types:
        class Checklist(Entity):
            # Automatically added by Django as related sets
            items: RelatedSet["Checklists.Types.ChecklistItem"] = []

        class ChecklistItem(Entity):
            name: str
            description: str
            is_completed: bool
            checklist: FK["Checklists.Types.Checklist"]

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
