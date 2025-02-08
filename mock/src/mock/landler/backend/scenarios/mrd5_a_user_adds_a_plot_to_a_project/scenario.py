from sunya import (
    goal,
    add_scenario,
    run_scenario,
    get_scenario,
    the,
    it,
    G as g,
    I as i,
    R as r,
)

scenario_name = f"backend/mrd5_a_user_adds_a_plot_to_a_project"


def start(variation="default"):
    with add_scenario(scenario_name):
        if variation == "default":
            # create a plot in the project
            with goal(i.create_a(r.plot).in_the(r.project)):
                with the(g.frontend).calls_the(g.create_plot_api_view):
                    with it().calls_the(g.create_plot_action):

                        # create the plot
                        with it().creates_the(r.plot).using_the(
                            r.polygon
                        ).that_is_taken_from_the(r.api_request):
                            assert r.plot.name == "my-plot"
                            assert r.plot.sequence_number
                            assert r.plot.polygon
                            assert r.plot.owner == g.user_session.active_organization

                        # create the plot questionnaire
                        with it().creates_the(r.plot_questionnaire):
                            assert r.plot.plot_questionnaire

                        # add the plot to the project
                        with goal(i.add_the(r.plot).to_the(r.project)):
                            with it().calls_the(g.add_plot_to_project_action):
                                with it().finds_the(r.default_plot_list).for_the(
                                    r.project
                                ):
                                    assert r.default_plot_list

                                with it().adds_the(r.plot).to_the(r.default_plot_list):
                                    pass

    return get_scenario(scenario_name)


def run():
    from ..mrd4_a_user_creates_a_project import scenario as mrd4_scenario

    run_scenario(mrd4_scenario)
    assert r.project

    return start()


if __name__ == "__main__":
    run()
