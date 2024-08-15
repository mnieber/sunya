from sunya import (
    add_goal,
    add_scenario,
    get_scenario,
    register,
    the,
    G as g,
    get_entities,
)
from landler.backend.modules.plot_lists import get_project_plot_list_by_name
import landler.backend.namespace as B


def start(project, variation="default"):
    scenario_name = "a-user-adds-a-plot-to-a-project"
    with add_scenario(scenario_name):
        e = get_entities()
        register(project, name="project")

        if variation == "default":
            with add_goal("create a", e.plot, "in the", e.project):
                with the(g.frontend).calls_the(g.create_plot_api_view):
                    with the(g.create_plot_api_view).calls_the(g.create_plot_action):
                        with the(g.create_plot_action).creates_the(e.plot):
                            plot_(e).plot_questionnaire = plot_questionnaire_(e)

                        with add_goal("add the", e.plot, "to the", e.project):
                            with the(g.create_plot_action).calls_the(
                                g.add_plot_to_project_action
                            ):
                                default_plot_list_(e).plots.append(e.plot)

    return get_scenario(scenario_name)


def default_plot_list_(e):
    return register(
        get_project_plot_list_by_name(e.project, "default"), name="default_plot_list"
    )


def plot_questionnaire_(e):
    return register(
        B.PlotQuestionnaires.Models.PlotQuestionnaire(
            land_type=B.PlotQuestionnaires.Enums.LandType.CROPLAND,
            plot=e.plot,
        ),
        name="plot_questionnaire",
    )


def plot_(e):
    return register(
        B.Plots.Models.Plot(
            name="my-plot",
            owner=g.user_session.active_organization,
            sequence_number=B.plot_sequence_number_generator.next(),
            polygon=B.Polygons.Models.Polygon(
                polygon="polygon",
                crc="",
                area=10.0,
            ),
        ),
        e.plot,
    )


def run():
    import landler.backend.scenarios.ms2_a_user_creates_a_project

    ms2_scenario = landler.backend.scenarios.ms2_a_user_creates_a_project.run()
    project = ms2_scenario.get_entity_by_name("project")

    return start(project=project)


if __name__ == "__main__":
    run()
