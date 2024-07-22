from landler.backend.app import *
from sunya import (
    add_scenario,
    get_entity,
    get_scenario,
)


def start(user, project, variation="default"):
    scenario_name = "a-user-schedule-a-project-analysis"
    with add_scenario(scenario_name):
        """
        Describe how we can replay events to bring a Project from its initial
        state to any of its successive states. At each iteration, the project should
        have the correct set of associated Plots at their respective iterations.
        """

    return get_scenario(scenario_name)


def run():
    import scenarios.s2_a_user_creates_a_project

    scenarios.s2_a_user_creates_a_project.run()
    user = get_entity(Users.Models.User, email="my-org-owner@example.com")
    project = get_entity(Projects.Models.Project, name="my-project")

    return start(user=user, project=project)


if __name__ == "__main__":
    run()
