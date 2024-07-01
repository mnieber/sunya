from domain.app import *
from domain.backend.modules.plot_lists.project_interface import (
    get_project_plot_list_by_name,
)
from domain.datatypes import *
from sunya import add_step, preregister, register


def the_create_plot_api_view_creates_a_plot_in_the_project(request, project):
    create_plot_form = Form(name="CreatePlotForm", data=request.data)
    p_plot = preregister("plot")

    with add_step(
        "The",
        create_plot_api_view,
        "calls the",
        create_plot_action,
        "with the",
        create_plot_form,
        "to create a",
        p_plot,
        "in the",
        project,
    ):
        with add_step("The", create_plot_action, "creates the", p_plot):
            plot = register(
                Plots.Models.Plot(
                    name="my-plot",
                    owner=user_session.active_organization,
                    sequence_number=plot_sequence_number_generator.next(),
                    polygon=Polygons.Models.Polygon(
                        polygon=request.data.get("polygon"), crc="", area=10.0
                    ),
                ),
                p_plot,
            )
            plot.plot_questionnaire = PlotQuestionnaires.Models.PlotQuestionnaire(
                land_type=PlotQuestionnaires.Enums.LandType.CROPLAND, plot=plot
            )

        with add_step(
            "The",
            create_plot_action,
            "calls the",
            add_plot_to_project_action,
            "to add the",
            plot,
            "to the",
            project,
        ):
            get_project_plot_list_by_name(project, "default").plots.append(plot)

    return plot
