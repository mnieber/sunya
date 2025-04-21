import mock.landler.frontend.namespace as F


def resolve_entity_in_global_namespace(name):
    if name == "organization_picker":
        return F.Organizations.Components.OrganizationPicker()

    if name == "get_checklist_query":
        return F.Checklists.Queries.GetChecklist()

    if name == "update_checklist_items_mutation":
        return F.Checklists.Mutations.UpdateChecklistItems()

    if name == "home_page_route":
        return F.Frames.Routes.HomePageRoute()

    return None
