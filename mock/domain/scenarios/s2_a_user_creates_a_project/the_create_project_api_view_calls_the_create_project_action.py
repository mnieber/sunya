from domain.app import *
from domain.datatypes import *
from sunya import add_step, preregister, register


def the_create_project_api_view_calls_the_create_project_action(request):
    create_project_form = Form(name="CreateProjectForm", data=request.data)
    project = preregister("project")

    with add_step(
        "The",
        create_project_api_view,
        "calls the",
        create_project_action,
        "with the",
        create_project_form,
        "to create a",
        project,
        "with admin",
        user_session.active_organization,
    ):
        with add_step("The", create_project_action, "creates the", project):
            project = register(Projects.Models.Project(name="my-project"), project)

        with add_step(
            "The",
            create_project_action,
            "calls the",
            add_organization_to_project_action,
            "to add the",
            user_session.active_organization,
            "to the",
            project,
        ):
            project.memberships.append(
                Projects.Models.ProjectMembership(
                    project=project,
                    organization=user_session.active_organization,
                    role=Projects.Enums.ProjectRoles.ADMIN,
                )
            )

    return project
