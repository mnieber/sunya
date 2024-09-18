from sunya import (
    add_scenario,
    run_scenario,
    get_scenario,
)


scenario_name = "backend/ms6-a-project-can-be-restored-to-a-previous-iteration"


def start(user, project, variation="default"):
    with add_scenario(scenario_name):
        """
        Describe how we can replay events to bring a Project from its initial
        state to any of its successive states. At each iteration, the project should
        have the correct set of associated Plots at their respective iterations.
        """

    return get_scenario(scenario_name)


def run():
    from . import ms2_a_user_creates_a_project

    ms2_scenario = run_scenario(ms2_a_user_creates_a_project)
    user = ms2_scenario.get_entity_by_name("user")
    project = ms2_scenario.get_entity_by_name("project")

    return start(user=user, project=project)


if __name__ == "__main__":
    run()
