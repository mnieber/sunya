from landler.backend.app import *
from sunya import add_scenario, get_entity, get_scenario, preregister, register, the
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
            _create_request()
            preregister("my_plot", name="plot")

            with add_goal("create a", e.plot, "in the", e.project):
                with the(frontend).calls_the(create_plot_api_view):
                    _create_the_create_plot_form(e)

                    with the(create_plot_api_view).calls_the(create_plot_action).with_the(e.create_plot_form):
                        with the(create_plot_action).creates_the(e.plot):
                            _create_plot(e)
                            _create_plot_questionnaire(e)
                            e.plot.plot_questionnaire = e.plot_questionnaire

                        with add_goal("add the", e.plot, "to the", e.project):
                            with the(create_plot_action).calls_the(add_plot_to_project_action):
                                _create_default_plot_list(e)
                                e.default_plot_list.plots.append(e.plot)

    return get_scenario(scenario_name)

def _create_default_plot_list(e):
    register(get_project_plot_list_by_name(e.project, "default"), name="default_plot_list")


def _create_the_create_plot_form(e):
    register(Form(name="CreatePlotForm", data=e.request.data), name="create_plot_form")


def _create_request():
    register(Request(endpoint="add-plot-to-project"), name="request")


def _create_plot_questionnaire(e):
    register(
        PlotQuestionnaires.Models.PlotQuestionnaire(
            land_type=PlotQuestionnaires.Enums.LandType.CROPLAND,
            plot=e.plot,
        ),
        name="plot_questionnaire",
    )


def _create_plot(e):
    register(Plots.Models.Plot(
        name="my-plot",
        owner=user_session.active_organization,
        sequence_number=plot_sequence_number_generator.next(),
        polygon=Polygons.Models.Polygon(
            polygon=e.request.data.get("polygon"),
            crc="",
            area=10.0,
        ),
        e.plot)
    )


def run():
    import landler.backend.scenarios.ms2_a_user_creates_a_project

    landler.backend.scenarios.ms2_a_user_creates_a_project.run()
    project = get_entity(Projects.Models.Project, name="my-project")

    return start(project=project)


if __name__ == "__main__":
    run()
