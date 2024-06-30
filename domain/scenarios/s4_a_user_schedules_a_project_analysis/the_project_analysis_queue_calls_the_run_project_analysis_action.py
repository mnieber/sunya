from mock.app import *
from mock.datatypes import *
from sunya import add_step, preregister, register


def the_project_analysis_queue_calls_the_run_project_analysis_action(project_analysis):
    with add_step(
        "the", project_analysis_queue, "calls the", run_project_analysis_action
    ):
        for plot_analysis in project_analysis.plot_analyses:
            with add_step(
                "the",
                run_project_analysis_action,
                "calls the",
                run_plot_analysis_action,
                "on a",
                plot_analysis,
                "in the",
                project_analysis,
            ):
                p_calcium_plot_analysis_job = preregister("calcium_job")
                with add_step(
                    "the",
                    run_plot_analysis_action,
                    "creates a",
                    p_calcium_plot_analysis_job,
                    "for the",
                    plot_analysis.plot,
                    "at the now timestamp of the",
                    plot_analysis,
                ):
                    plot_at_now = register(
                        at_ts(plot_analysis.plot, plot_analysis.now), name="plot_at_now"
                    )

                    calcium_plot_analysis_job = register(
                        CalciumPlotAnalysisJob(
                            project_analysis_id=project_analysis.id,
                            polygon=plot_at_now.polygon,
                        ),
                        p_calcium_plot_analysis_job,
                    )
                    assert calcium_plot_analysis_job
