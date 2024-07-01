from domain.app import *
from domain.backend.modules.plot_lists.project_interface import (
    get_project_plot_list_by_name,
)
from domain.datatypes import *
from sunya import (
    add_scenario,
    add_step,
    get_entity,
    get_scenario,
    preregister,
    register,
)


def start(user, project, variation="default"):
    scenario_name = "a-user-schedule-a-project-analysis"
    with add_scenario(scenario_name):
        pass
        """
        Describe how existing PlotAnalyses can still continue to run if the
        previous calcium server url is still available. However, if the previous server
        is brought down then these PlotAnalyses will be restarted from scratch on the
        new calcium server.
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
