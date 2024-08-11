from landler.backend.app import *
from sunya import (
    add_goal,
    add_scenario,
    add_step,
    get_entities,
    get_entity,
    get_scenario,
    List,
    preregister,
    register,
)

from sunya.utils import get_time


def start(project, variation="default"):
    scenario_name = "a-user-schedules-a-project-analysis"
    with add_scenario(scenario_name):
        e = get_entities()
        register(project, alias="project")

        preregister("project_analysis_job")
        with add_goal("create a", e.project_analysis_job):
            with frontend.calls(create_project_analysis_job_api_view):
                with create_project_analysis_job_api_view.calls(
                    create_project_analysis_job_action
                ):
                    with create_project_analysis_job_action.creates(
                        e.project_analysis_job
                    ):
                        _create_project_analysis_job(e)

        preregister("jobs_to_run")
        with add_step("the", project_analysis_queue, "finds", e.jobs_to_run):
            _create_jobs_to_run(e)

        for idx, project_analysis_job in enumerate(e.jobs_to_run.items):
            with add_step(
                "the",
                project_analysis_queue,
                f"runs the {ith(idx)}",
                project_analysis_job,
            ):
                preregister("project_analysis")

                with add_goal(
                    "create a", e.project_analysis, "from a", e.project_analysis_job
                ):
                    with project_analysis_queue.calls(create_project_analysis_action):
                        _create_project_analysis(e, project_analysis_job)
                        e.project_analysis_job.project_analyses.append(
                            e.project_analysis
                        )

                        with add_step(
                            "the",
                            create_project_analysis_action,
                            "gets the",
                            e.project_analysis.project,
                            "at the now ts of the",
                            e.project_analysis,
                        ):
                            _create_project_at_now()

                        with add_step(
                            "the",
                            create_project_analysis_action,
                            "loops over all plots in the",
                            e.project_at_now,
                        ):
                            plot_list = get_project_plot_list_by_name(
                                e.project_at_now, "default"
                            )
                            for plot in plot_list.plots:
                                preregister("plot_analysis")

                                with add_goal(
                                    "add a ",
                                    e.plot_analysis,
                                    "for the",
                                    plot,
                                    "to the",
                                    e.project_analysis,
                                ):
                                    with create_project_analysis_action.creates(
                                        e.plot_analysis
                                    ):
                                        _create_plot_analysis(e, plot)
                                        e.project_analysis.plot_analyses.append(
                                            e.plot_analysis
                                        )

                with add_goal(
                    "run each",
                    e.plot_analysis,
                    "in the",
                    e.project_analysis,
                    "for the",
                    e.plot_analysis.plot,
                    "at the now timestamp of the",
                    e.plot_analysis,
                ):
                    with add_step(
                        "the",
                        e.project_analysis_queue,
                        "calls the",
                        run_project_analysis_action,
                    ):
                        for plot_analysis in e.project_analysis.plot_analyses:
                            with run_project_analysis_action.calls(
                                run_plot_analysis_action
                            ).wth(plot_analysis):
                                preregister("calcium_job")

                                with run_plot_analysis_action.creates(
                                    e.calcium_plot_analysis_job
                                ):
                                    plot_at_now = _create_plot_at_now(plot_analysis)
                                    _create_calcium_plot_analysis_job(
                                        e, plot_analysis, plot_at_now
                                    )

            for idx, plot_analysis in enumerate(e.project_analysis.plot_analyses):
                # TODO: the_backend_processes_a_calcium_job_result(idx, plot_analysis)
                pass

    return get_scenario(scenario_name)


def _create_calcium_plot_analysis_job(e, plot_analysis, plot_at_now):
    calcium_plot_analysis_job = register(
        CalciumPlotAnalysisJob(
            id=plot_analysis.id,
            polygon=plot_at_now.polygon,
        ),
        e.calcium_plot_analysis_job,
    )

    return calcium_plot_analysis_job


def _create_plot_at_now(plot_analysis):
    plot_at_now = register(
        at_ts(plot_analysis.plot, plot_analysis.now),
        name="plot_at_now",
    )

    return plot_at_now


def _create_plot_analysis(e, plot):
    register(
        PlotAnalyses.Models.PlotAnalysis(
            plot=plot,
            project_analysis=project_analysis,
            now=project_analysis.now,
            status=PlotAnalyses.Enums.PlotAnalysisStatus.RUNNING,
        ),
        e.plot_analysis,
    )


def _create_project_at_now():
    register(
        at_ts(project_analysis.project, project_analysis.now),
        name="project_at_now",
    )


def _create_project_analysis(e, project_analysis_job):
    register(
        ProjectAnalyses.Models.ProjectAnalysis(
            job=project_analysis_job,
            project=project_analysis_job.project,
            now=project_analysis_job.scheduled_at,
            status=ProjectAnalyses.Enums.ProjectAnalysisStatus.RUNNING,
        ),
        e.project_analysis,
    )


def _create_jobs_to_run(e):
    register(
        List(name="jobs_to_run", items=[e.project_analysis_job]),
        e.jobs_to_run,
    )


def _create_project_analysis_job(e):
    register(
        ProjectAnalysisJobs.Models.ProjectAnalysisJob(
            project=e.project,
            scheduled_at=get_time.now(bump=True),
        ),
        e.project_analysis_job,
    )


def run():
    import landler.backend.scenarios.ms3_a_user_adds_a_plot_to_a_project

    landler.backend.scenarios.ms3_a_user_adds_a_plot_to_a_project.run()
    project = get_entity(Projects.Models.Project, name="my-project")

    return start(project=project)


if __name__ == "__main__":
    run()
