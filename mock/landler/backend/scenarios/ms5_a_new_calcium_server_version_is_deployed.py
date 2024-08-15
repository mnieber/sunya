from sunya import (
    add_scenario,
    get_scenario,
)


def start(user, project, variation="default"):
    scenario_name = "a-user-schedule-a-project-analysis"
    with add_scenario(scenario_name):
        """
        Describe how existing PlotAnalyses can still continue to run if the
        previous calcium server url is still available. However, if the previous server
        is brought down then these PlotAnalyses will be restarted from scratch on the
        new calcium server.
        """

    return get_scenario(scenario_name)


def run():
    import scenarios.s2_a_user_creates_a_project

    ms2_scenario = scenarios.s2_a_user_creates_a_project.run()
    user = ms2_scenario.get_entity_by_name("user")
    project = ms2_scenario.get_entity_by_name("project")

    return start(user=user, project=project)


if __name__ == "__main__":
    run()
