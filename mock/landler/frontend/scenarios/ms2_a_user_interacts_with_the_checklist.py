import landler.frontend.namespace as F
from sunya import (
    add_goal,
    add_scenario,
    add_step,
    get_entities,
    get_scenario,
    register,
    the,
    G as g,
)


def start(user):
    scenario_name = "ms2-a-user-interacts-with-the-checklist"
    register(user, name="user")

    with add_scenario(scenario_name):
        e = get_entities()
        register(user, name="user")

        with the(e.user).signs_in():
            pass

        with the(e.user).is_redirected_to(g.home_page_route):
            with add_goal("load the", e.checklist):
                with the(g.frontend).calls_the(g.get_checklist_query):
                    _create_checklist()

        with the_user_views_checklist():
            pass

        item_to_complete = e.checklist[0]
        with add_goal("The", e.user, "clicks to complete the", item_to_complete):
            with the(g.frontend).calls_the(g.update_checklist_items_mutation):
                item_to_complete.is_completed = True

    return get_scenario(scenario_name)


def _create_checklist():
    register(
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


def the_user_views_checklist():
    return add_step(
        "The",
        e.user,
        "views the",
        e.checklist,
        "on the home page",
    )


def run():
    user = F.Users.Types.User(email="alice@example.com")
    return start(user)


if __name__ == "__main__":
    run()
