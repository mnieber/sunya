from landler.backend.app import *
from sunya import (
    add_goal,
    add_scenario,
    get_entity,
    get_scenario,
    register,
    the,
)
from landler.backend.modules.plot_lists import (
    get_project_plot_list_by_name,
)
from sunya.scenarios.store import get_entities


def start(project, variation="default"):
    scenario_name = "a-user-adds-a-plot-to-a-project"
    with add_scenario(scenario_name):
        e = get_entities()
        register(project, name="project")

        if variation == "default":
            with add_goal("create a", e.plot, "in the", e.project):
                with the(frontend).calls_the(create_plot_api_view):
                    with the(create_plot_api_view).calls_the(create_plot_action):
                        with the(create_plot_action).creates_the(e.plot):
                            plot_(e).plot_questionnaire = plot_questionnaire_(e)

                        with add_goal("add the", e.plot, "to the", e.project):
                            with the(create_plot_action).calls_the(
                                add_plot_to_project_action
                            ):
                                default_plot_list_(e).plots.append(e.plot)

    return get_scenario(scenario_name)


def default_plot_list_(e):
    register(
        get_project_plot_list_by_name(e.project, "default"), name="default_plot_list"
    )


def plot_questionnaire_(e):
    register(
        PlotQuestionnaires.Models.PlotQuestionnaire(
            land_type=PlotQuestionnaires.Enums.LandType.CROPLAND,
            plot=e.plot,
        ),
        name="plot_questionnaire",
    )


def plot_(e):
    register(
        Plots.Models.Plot(
            name="my-plot",
            owner=user_session.active_organization,
            sequence_number=plot_sequence_number_generator.next(),
            polygon=Polygons.Models.Polygon(
                polygon=e.request.data.get("polygon"),
                crc="",
                area=10.0,
            ),
        ),
        e.plot,
    )


def run():
    import landler.backend.scenarios.ms2_a_user_creates_a_project

    landler.backend.scenarios.ms2_a_user_creates_a_project.run()
    project = get_entity(Projects.Models.Project, name="my-project")

    return start(project=project)


if __name__ == "__main__":
    run()
