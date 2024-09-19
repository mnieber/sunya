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
    checklist = add_role(name="Checklist")

    with add_scenario(scenario_name):
        user.actor = add_actor(a_user, name="user")

        with the(user).signs_in():
            pass

        with the(user).is_redirected_to(g.home_page_route):
            with add_goal("load the", checklist):
                with the(g.frontend).calls_the(g.get_checklist_query):
                    checklist.actor = checklist_()

        with the(user).views_the(checklist).on_the(g.home_page_route):
            pass

        item_to_complete = checklist.actor.items[0]
        with add_goal("The", user, "clicks to complete the", item_to_complete):
            with the(g.frontend).calls_the(g.update_checklist_items_mutation):
                item_to_complete.is_completed = True

    return get_scenario(scenario_name)


def checklist_():
    return add_actor(
        F.Checklist.Types.Checklist(
            items=[
                F.Checklist.Types.ChecklistItem(
                    title="Add your organization",
                    description="Set up your organization details",
                    is_completed=False,
                ),
                F.Checklist.Types.ChecklistItem(
                    title="Create a project",
                    description="Start your first project",
                    is_completed=False,
                ),
                F.Checklist.Types.ChecklistItem(
                    title="Add a plot",
                    description="Create your first plot",
                    is_completed=False,
                ),
                F.Checklist.Types.ChecklistItem(
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
