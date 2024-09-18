import darshana.frontend.namespace as F
from sunya import (
    add_goal,
    add_scenario,
    get_scenario,
    add_actor,
    add_role,
    the,
    G as g,
)


def start(user):
    project = add_role("Project")

    scenario_name = "ms1-a-user-creates-a-project"
    with add_scenario(scenario_name):
        add_actor(user, name="user", role="User")

        with add_goal("create a new", project, "for the", g.user):
            with the(g.user).visits_the(g.projects_route):
                pass

            with the(g.user).presses_the(g.create_project_button):
                pass

            with the(g.user).enters_the_project_name():
                pass

            with the(g.user).submits_the(g.project_lead_form_view):
                with the(g.frontend).calls_the(g.create_project_mutation):
                    project_()

            with the(g.frontend).redirects_to_the(g.project_route):
                pass

        with add_goal("delete a", project, "for the", g.user):
            with the(g.user).visits_the(g.projects_route):
                pass

            with the(g.user).presses_the(g.delete_project_button):
                with the(g.frontend).asks_confirmation_from_the(g.user):
                    pass

                with the(g.frontend).calls_the(g.delete_project_mutation):
                    pass

    return get_scenario(scenario_name)


def project_():
    add_actor(
        F.Projects.Types.Project(
            name="My Darshana Project",
            scenarios=[
                F.Scenarios.Types.Scenario(
                    name="My First",
                    root_step=F.Steps.Types.Step(
                        fact=("Root",),
                        child_steps=[
                            F.Steps.Types.Step(
                                fact=("Base Step 1",),
                                child_steps=[
                                    F.Steps.Types.Step(fact=("Child Step 1",))
                                ],
                            ),
                            F.Steps.Types.Step(fact=("Root Step 2",)),
                        ],
                    ),
                )
            ],
        ),
        name="project",
        role="Project",
    )


def run():
    user = F.Users.Types.User(email="alice@example.com")

    return start(user)


if __name__ == "__main__":
    run()
