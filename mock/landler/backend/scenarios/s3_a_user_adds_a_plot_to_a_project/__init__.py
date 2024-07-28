from landler.backend.app import *
from sunya import add_scenario, add_step, get_entity, get_scenario

from .the_create_plot_api_view_creates_a_plot_in_the_project import (
    the_create_plot_api_view_creates_a_plot_in_the_project,
)


def start(project, variation="default"):
    scenario_name = "a-user-adds-a-plot-to-a-project"
    with add_scenario(scenario_name):

        if variation == "default":
            request = Request(endpoint="add-plot-to-project")
            with the_fe_posts_to_create_a_plot(request):
                plot = the_create_plot_api_view_creates_a_plot_in_the_project(
                    request, project
                )
                assert plot

    return get_scenario(scenario_name)


def the_fe_posts_to_create_a_plot(request):
    return add_step(
        "The",
        frontend,
        "calls the",
        create_plot_api_view,
    )


def run():
    import landler.backend.scenarios.s2_a_user_creates_a_project

    landler.backend.scenarios.s2_a_user_creates_a_project.run()
    project = get_entity(Projects.Models.Project, name="my-project")

    return start(project=project)


if __name__ == "__main__":
    run()
