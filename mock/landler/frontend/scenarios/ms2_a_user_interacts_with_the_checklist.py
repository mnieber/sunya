import landler.frontend.namespace as F
from sunya import (
    add_goal,
    add_scenario,
    add_actor,
    get_scenario,
    add_role,
    the,
    G as g,
)


scenario_name = "frontend/ms2-a-user-interacts-with-the-checklist"


def start(a_user):
    user = add_role(name="User")

    with add_scenario(scenario_name):
        user.actor = add_actor(a_user, name="user")

        with the(user).signs_in():
            pass

        with the(user).is_redirected_to(g.home_page_route):
            with add_goal("load the", g.checklist):
                with the(g.frontend).calls_the(g.get_checklist_query):
                    _create_checklist()

        with the(user).views_the(g.checklist).on_the(g.home_page):
            pass

        item_to_complete = e.checklist[0]
        with add_goal("The", e.user, "clicks to complete the", item_to_complete):
            with the(g.frontend).calls_the(g.update_checklist_items_mutation):
                item_to_complete.is_completed = True

    return get_scenario(scenario_name)


def _create_checklist():
    return add_actor(
        F.Checklist.Types.Checklist(
            items=[
                F.Checklist.Types.ChecklistItem(
                    id="1",
                    title="Add your organization",
                    description="Set up your organization details",
                    is_completed=False,
                ),
                F.Checklist.Types.ChecklistItem(
                    id="2",
                    title="Create a project",
                    description="Start your first project",
                    is_completed=False,
                ),
                F.Checklist.Types.ChecklistItem(
                    id="3",
                    title="Add a plot",
                    description="Create your first plot",
                    is_completed=False,
                ),
                F.Checklist.Types.ChecklistItem(
                    id="4",
                    title="Trigger a project-analysis",
                    description="Analyze your project data",
                    is_completed=False,
                ),
            ]
        ),
        name="checklist",
    )


def run():
    user = F.Users.Types.User(email="alice@example.com")
    return start(user)


if __name__ == "__main__":
    run()
