import darshana.frontend.namespace as F
from sunya import (
    add_goal,
    add_scenario,
    get_scenario,
    register,
    the,
    G as g,
    get_entities,
)


def start(user):
    scenario_name = "ms1-a-user-creates-a-project"
    with add_scenario(scenario_name):
        e = get_entities()
        register(user, name="user")

        with add_goal("create a new", e.project, "for the", e.user):
            with the(e.user).visits_the(g.projects_route):
                pass

            with the(e.user).enters_project_name():
                pass

            with the(e.user).presses_the(g.import_files_button):
                with the(g.frontend).uploads_spec_files():
                    pass

            with the(e.user).deletes_some_uploaded_files():
                pass

            with the(e.user).presses_the(g.create_project_button):
                with the(g.frontend).calls_the(g.create_project_mutation):
                    project_(e)

            with the(g.frontend).redirects_to_the(g.project_route):
                pass

    return get_scenario(scenario_name)


def project_(e):
    return register(
        F.Projects.Types.Project(
            name="My Darshana Project",
        ),
        e.project,
    )


def run():
    user = F.Users.Types.User(email="alice@example.com")

    return start(user)


if __name__ == "__main__":
    run()
