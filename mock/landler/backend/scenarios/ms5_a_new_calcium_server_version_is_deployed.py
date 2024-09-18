from sunya import (
    add_scenario,
    run_scenario,
    get_scenario,
)


scenario_name = "backend/ms5-a-new-calcium-server-version-is-deployed"


def start(user, project, variation="default"):
    with add_scenario(scenario_name):
        """
        Describe how existing PlotAnalyses can still continue to run if the
        previous calcium server url is still available. However, if the previous server
        is brought down then these PlotAnalyses will be restarted from scratch on the
        new calcium server.
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
un
