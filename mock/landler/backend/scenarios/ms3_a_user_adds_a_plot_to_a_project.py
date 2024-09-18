from sunya import (
    add_goal,
    add_scenario,
    get_scenario,
    add_role,
    the,
    G as g,
    add_actor,
)
from landler.backend.modules.plot_lists import get_project_plot_list_by_name
import landler.backend.namespace as B


scenario_name = "backend/ms3-a-user-adds-a-plot-to-a-project"


def start(a_project, variation="default"):
    project = add_role("Project")
    plot = add_role("Plot")

    with add_scenario(scenario_name):
        project.actor = add_actor(a_project, name="project")

        if variation == "default":
            with add_goal("create a", plot, "in the", project):
                with the(g.create_plot_action).creates_the(plot):
                    plot.actor = plot_()
                    plot_questionnaire_()
                    g.plot.plot_questionnaire = g.plot_questionnaire

                with add_goal("add the", plot, "to the", project):
                    with the(g.create_plot_action).calls_the(
                        g.add_plot_to_project_action
                    ):
                        default_plot_list_()
                        g.default_plot_list.plots.append(g.plot)

    return get_scenario(scenario_name)


def default_plot_list_():
    add_actor(
        get_project_plot_list_by_name(g.project, "default"), name="default_plot_list"
    )


def plot_questionnaire_():
    return add_actor(
        B.PlotQuestionnaires.Models.PlotQuestionnaire(
            land_type=B.PlotQuestionnaires.Enums.LandType.CROPLAND,
            plot=g.plot,
        ),
        name="plot_questionnaire",
    )


def plot_():
    return add_actor(
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
        name="plot",
    )


def run():
    import landler.backend.scenarios.ms2_a_user_creates_a_project

    ms2_scenario = landler.backend.scenarios.ms2_a_user_creates_a_project.run()
    project = ms2_scenario.get_entity_by_name("project")

    return start(a_project=project)


if __name__ == "__main__":
    run()
