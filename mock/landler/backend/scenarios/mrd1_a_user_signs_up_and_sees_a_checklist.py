import landler.backend.namespace as B
import landler.frontend.namespace as F  # noqa

from sunya import (
    add_goal,
    add_scenario,
    add_role,
    add_actor,
    get_scenario,
    get_scenario_name,
    the,
    G as g,
)


scenario_name = f"backend/{get_scenario_name(__file__)}"


def start():
    user = add_role("User")
    checklist = add_role("Checklist")

    with add_scenario(scenario_name):
        with add_goal("sign up as a", user):
            with the(g.sign_up_user_api_view).calls_the(g.create_user_action):
                with the(g.create_user_action).creates_the(user):
                    user.actor = user_()

            with the(g.sign_up_user_api_view).activates_the_account_of_the(user):
                g.user.is_active = True

        with add_goal("create a", checklist, "for the", user):
            with the(g.sign_up_user_api_view).calls_the(g.create_checklist_action):
                with the(g.create_checklist_action).creates_the(checklist):
                    checklist.actor = checklist_()
                    user.actor.checklist = checklist.actor

        with add_goal("sign in as a", user):
            with the(g.sign_in_user_api_view).calls_the(g.sign_in_user_action):
                g.user_session.user = g.user
                g.user.is_authenticated = True

    return get_scenario(scenario_name)


def user_():
    return add_actor(
        B.Users.Models.User(
            email="my-org-owner@example.com",
            password="my-password",
        ),
        name="user",
    )


def checklist_():
    return add_actor(
        B.Checklists.Models.Checklist(
            owner=g.user,
            items=[
                B.Checklists.Models.ChecklistItem(
                    title="Welcome",
                    description="Welcome to the application",
                    is_completed=False,
                ),
                B.Checklists.Models.ChecklistItem(
                    title="Join the demo org",
                    description="Join the demo organization",
                    is_completed=False,
                ),
                B.Checklists.Models.ChecklistItem(
                    title="Add your organization",
                    description="Create your own organization",
                    is_completed=False,
                ),
                B.Checklists.Models.ChecklistItem(
                    title="Create a project",
                    description="Start your first project",
                    is_completed=False,
                ),
                B.Checklists.Models.ChecklistItem(
                    title="Add a plot",
                    description="Add your first plot to the project",
                    is_completed=False,
                ),
                B.Checklists.Models.ChecklistItem(
                    title="Trigger a project-analysis",
                    description="Run your first project analysis",
                    is_completed=False,
                ),
            ],
        ),
        name="checklist",
    )


def run():
    return start()


if __name__ == "__main__":
    run()
