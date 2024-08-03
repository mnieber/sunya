from landler.frontend.app import *
from sunya import add_scenario, add_step, get_scenario, register


def start(user):
    scenario_name = "ms2-a-user-signs-in"
    with add_scenario(scenario_name):
        with the_user_signs_in(user):
            pass

        with the_user_is_redirected_to_home_page(user):
            checklist = the_frontend_loads_checklist()

        with the_user_views_checklist(user, checklist):
            pass

        with the_user_minimizes_or_completes_a_checklist_item(user, checklist):
            pass

    return get_scenario(scenario_name)


def the_user_signs_in(user):
    return add_step(
        "The",
        user,
        "signs in",
    )


def the_user_is_redirected_to_home_page(user):
    return add_step(
        "The",
        user,
        "is redirected to the",
        home_page_route,
    )


def the_frontend_loads_checklist():
    with add_step(
        "The",
        frontend,
        "calls the",
        get_checklist_query,
        "to load the checklist",
    ):
        checklist = register(
            [
                Checklist.Types.ChecklistItem(
                    id="1",
                    title="Add your organization",
                    description="Set up your organization details",
                    is_completed=False,
                ),
                Checklist.Types.ChecklistItem(
                    id="2",
                    title="Create a project",
                    description="Start your first project",
                    is_completed=False,
                ),
                Checklist.Types.ChecklistItem(
                    id="3",
                    title="Add a plot",
                    description="Create your first plot",
                    is_completed=False,
                ),
                Checklist.Types.ChecklistItem(
                    id="4",
                    title="Trigger a project-analysis",
                    description="Analyze your project data",
                    is_completed=False,
                ),
            ]
        )
    return checklist


def the_user_views_checklist(user, checklist):
    return add_step(
        "The",
        user,
        "views the",
        checklist,
        "on the home page",
    )


def the_user_completes_a_checklist_item(user, checklist):
    item_to_complete = checklist[0]
    step = add_step(
        "The",
        user,
        "completes the checklist item",
        item_to_complete,
        "using the",
        update_checklist_items_mutation,
    )
    with step:
        item_to_complete.is_completed = True

    return step


def run():
    user = Users.Types.User(email="alice@example.com")
    return start(user)


if __name__ == "__main__":
    run()
