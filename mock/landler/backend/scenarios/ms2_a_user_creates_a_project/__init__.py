from landler.backend.app import *
from sunya import add_scenario, add_step, get_scenario

from .the_create_project_api_view_calls_the_create_project_action import (
    the_create_project_api_view_calls_the_create_project_action,
)


def start():
    scenario_name = "a-user-creates-a-project"
    with add_scenario(scenario_name):
        request = Request(endpoint="create-project")

        with the_fe_posts_to_create_a_project(request):
            project = the_create_project_api_view_calls_the_create_project_action(
                request
            )
            assert project

    return get_scenario(scenario_name)


def the_fe_posts_to_create_a_project(request):
    return add_step(
        "The",
        frontend,
        "calls the",
        create_project_api_view,
    )


def run():
    import landler.backend.scenarios.ms1_a_user_signs_up_and_creates_an_org

    landler.backend.scenarios.ms1_a_user_signs_up_and_creates_an_org.run()

    return start()


if __name__ == "__main__":
    run()
