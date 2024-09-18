import landler.backend.namespace as B
from sunya import (
    add_goal,
    add_scenario,
    add_actor,
    get_scenario,
    add_role,
    the,
    G as g,
)


def start():
    project = add_role("Project")

    scenario_name = "a-user-creates-a-project"
    with add_scenario(scenario_name):
        with the(g.frontend).calls_the(g.create_project_api_view):
            with add_goal(
                "create a",
                project,
                "with admin",
                g.user_session.active_organization,
            ):
                with the(g.create_project_api_view).calls_the(g.create_project_action):
                    with the(g.create_project_action).creates_the(project):
                        project_()

            with add_goal(
                "add the", g.user_session.active_organization, "to the", g.project
            ):
                with the(g.create_project_action).calls_the(
                    g.add_organization_to_project_action
                ):
                    project_membership_()
                    g.project.memberships.append(g.project_membership)

    return get_scenario(scenario_name)


def project_():
    add_actor(
        B.Projects.Models.Project(name="my-project"), name="project", role="Project"
    )


def project_membership_():
    add_actor(
        B.Projects.Models.ProjectMembership(
            project=g.project,
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
