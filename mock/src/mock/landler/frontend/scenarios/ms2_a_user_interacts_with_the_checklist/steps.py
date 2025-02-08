from sunya import R as r, G as g, match_step as match, the
import mock.landler.frontend.namespace as F


def implement_step(step):
    if match(step, the(r.user).signs_in()):
        r.user = F.Users.Types.User(email="alice@example.com")

    elif match(step, the(g.frontend).calls_the(g.get_checklist_query)):
        r.checklist = F.Checklists.Types.Checklist(items=[])

        for name, description in [
            ("Add your organization", "Set up your organization details"),
            ("Create a project", "Start your first project"),
            ("Add a plot", "Create your first plot"),
            ("Trigger a project-analysis", "Analyze your project data"),
        ]:
            r.checklist.items.append(
                F.Checklists.Types.ChecklistItem(
                    name=name,
                    description=description,
                    is_completed=False,
                    checklist=r.checklist,
                ),
            )

        r.first_item_to_complete = r.checklist.items[0]

    elif match(step, the(g.frontend).calls_the(g.update_checklist_items_mutation)):
        r.checklist.items[0].is_completed = True
