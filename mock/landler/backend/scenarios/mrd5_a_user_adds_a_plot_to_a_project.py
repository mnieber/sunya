from sunya import (
    add_goal,
    add_scenario,
    run_scenario,
    get_scenario,
    get_scenario_name,
    add_role,
    the,
    G as g,
    add_actor,
)
from landler.backend.modules.plot_lists import get_project_plot_list_by_name
import landler.backend.namespace as B


scenario_name = f"backend/{get_scenario_name(__file__)}"


def start(a_project, variation="default"):
    project = add_role("Project")
    plot = add_role("Plot")
    plot_questionnaire = add_role("PlotQuestionnaire")

    with add_scenario(scenario_name):
        project.actor = add_actor(a_project, name="project")

        if variation == "default":
            with add_goal("create a", plot, "in the", project):
                with the(g.create_plot_action).creates_the(plot).and_its(
                    plot_questionnaire
                ):
                    plot.actor = plot_()
                    plot_questionnaire.actor = plot_questionnaire_()
                    plot.actor.plot_questionnaire = plot_questionnaire.actor

                with add_goal("add the", plot, "to the", project):
                    with the(g.create_plot_action).calls_the(
                        g.add_plot_to_project_action
                    ):
                        default_plot_list_()
                        g.default_plot_list.plots.append(g.plot)

    return get_scenario(scenario_name)


def default_plot_list_():
    return add_actor(
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
    from . import mrd4_a_user_creates_a_project

    mrd4_scenario = run_scenario(mrd4_a_user_creates_a_project)
    project = mrd4_scenario.get_entity_by_name("project")

    return start(a_project=project)


if __name__ == "__main__":
    run()
