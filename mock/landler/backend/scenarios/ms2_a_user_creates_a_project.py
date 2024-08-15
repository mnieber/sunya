import landler.backend.namespace as B
from sunya import (
    add_goal,
    add_scenario,
    get_entities,
    get_scenario,
    register,
    the,
    G as g,
)


def start():
    scenario_name = "a-user-creates-a-project"
    with add_scenario(scenario_name):
        e = get_entities()

        with the(g.frontend).calls_the(g.create_project_api_view):
            with add_goal(
                "create a",
                e.project,
                "with admin",
                g.user_session.active_organization,
            ):
                with the(g.create_project_api_view).calls_the(g.create_project_action):
                    with the(g.create_project_action).creates_the(e.project):
                        project_(e)

            with add_goal(
                "add the", g.user_session.active_organization, "to the", e.project
            ):
                with the(g.create_project_action).calls_the(
                    g.add_organization_to_project_action
                ):
                    e.project.memberships.append(project_membership_(e))

    return get_scenario(scenario_name)


def project_(e):
    register(B.Projects.Models.Project(name="my-project"), e.project)


def project_membership_(e):
    register(
        B.Projects.Models.ProjectMembership(
            project=e.project,
            organization=g.user_session.active_organization,
            role=B.Projects.Enums.OrganizationInProjectRoles.ADMIN,
        ),
        name="project_membership",
    )


def run():
    import landler.backend.scenarios.ms1_a_user_signs_up_and_creates_an_org

    landler.backend.scenarios.ms1_a_user_signs_up_and_creates_an_org.run()

    return start()


if __name__ == "__main__":
    run()
