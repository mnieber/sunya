from domain.app import *
from sunya import add_step, preregister, register


def the_project_analysis_queue_creates_a_calcium_plot_analysis_job(project_analysis):
    p_calcium_plot_analysis_job = preregister("calcium_plot_analysis_job")
    with add_step(
        "The",
        project_analysis_queue,
        "creates a",
        p_calcium_plot_analysis_job,
    ):
        calcium_plot_analysis_job = register(
            CalciumPlotAnalysisJob(project_analysis_id=project_analysis.id),
            p_calcium_plot_analysis_job,
        )

    return calcium_plot_analysis_job
