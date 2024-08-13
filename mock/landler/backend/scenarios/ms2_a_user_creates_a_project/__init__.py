from landler.backend.app import *
from sunya import add_goal, add_scenario, get_entities, get_scenario, preregister, the


def start():
    scenario_name = "a-user-creates-a-project"
    with add_scenario(scenario_name):
        e = get_entities()
        _create_request()

        with the(frontend).calls_the(create_project_api_view).with_the(e.request):
            preregister("project")

            with add_goal(
                "create a", e.project, "with admin", user_session.active_organization
            ):
                _create_the_create_project_form()

                with the(create_project_api_view).calls_the(
                    create_project_action
                ).with_the(e.create_project_form):
                    with the(create_project_action).creates_the(e.project):
                        _create_project(e)

            with add_goal(
                "add the", user_session.active_organization, "to the", e.project
            ):
                with the(create_project_action).calls_the(
                    add_organization_to_project_action
                ):
                    _create_project_membership(e.project)
                    e.project.memberships.append(e.project_membership)

    return get_scenario(scenario_name)


def _create_request():
    register(Request(endpoint="create-project"), name="request")


def _create_project(e):
    register(Projects.Models.Project(name="my-project"), e.project)


def _create_the_create_project_form(e):
    register(
        Form(name="CreateProjectForm", data=e.request.data),
        name="create_project_form",
    )


def _create_project_membership():
    register(
        Projects.Models.ProjectMembership(
            project=e.project,
            organization=user_session.active_organization,
            role=Projects.Enums.OrganizationInProjectRoles.ADMIN,
        ),
        name="project_membership",
    )


def run():
    import landler.backend.scenarios.ms1_a_user_signs_up_and_creates_an_org

    landler.backend.scenarios.ms1_a_user_signs_up_and_creates_an_org.run()

    return start()


if __name__ == "__main__":
    run()
