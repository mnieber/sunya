from domain.app import *
from domain.backend.modules.plot_lists.project_interface import (
    get_project_plot_list_by_name,
)
from domain.datatypes import *
from sunya import add_step, create_uuid, preregister, register


def the_project_analysis_queue_calls_the_create_project_analysis_action(
    project_analysis_job,
):
    p_project_analysis = preregister("project_analysis")

    with add_step(
        "The",
        project_analysis_queue,
        "calls the",
        create_project_analysis_action,
        "to create a",
        p_project_analysis,
        "from a",
        project_analysis_job,
    ):
        project_analysis = register(
            ProjectAnalyses.Models.ProjectAnalysis(
                id="98a05401-e76e-5e9c-bd3f-d15b567d1dce",
                job=project_analysis_job,
                project=project_analysis_job.project,
                now=project_analysis_job.scheduled_at,
                status=ProjectAnalyses.Enums.ProjectAnalysisStatus.RUNNING,
            ),
            p_project_analysis,
        )
        project_analysis_job.project_analyses.append(project_analysis)

        with add_step(
            "the",
            create_project_analysis_action,
            "gets the",
            project_analysis.project,
            "at the now ts of the",
            project_analysis,
        ):
            project_at_now = register(
                at_ts(project_analysis.project, project_analysis.now),
                name="project_at_now",
            )

        with add_step(
            "the",
            create_project_analysis_action,
            "loops over all plots in the",
            project_at_now,
        ):
            plot_list = get_project_plot_list_by_name(project_at_now, "default")
            for plot in plot_list.plots:
                plot_analysis = the_create_project_analysis_action_calls_the_create_plot_analysis_action(
                    project_analysis, plot
                )
                project_analysis.plot_analyses.append(plot_analysis)

        return project_analysis


def the_create_project_analysis_action_calls_the_create_plot_analysis_action(
    project_analysis, plot
):
    p_plot_analysis = preregister("plot_analysis")
    with add_step(
        "the",
        create_project_analysis_action,
        "creates a",
        p_plot_analysis,
        "for the",
        plot,
    ):
        plot_analysis = register(
            PlotAnalyses.Models.PlotAnalysis(
                id=create_uuid(),
                plot=plot,
                project_analysis=project_analysis,
                now=project_analysis.now,
                status=PlotAnalyses.Enums.PlotAnalysisStatus.RUNNING,
            ),
            p_plot_analysis,
        )

    return plot_analysis
