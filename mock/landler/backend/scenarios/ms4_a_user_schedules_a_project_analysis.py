from landler.backend.app import *
from sunya import (
    add_goal,
    add_scenario,
    add_step,
    get_entities,
    get_entity,
    get_scenario,
    List,
    register,
    the,
)

from sunya.utils import get_time


def start(project, variation="default"):
    scenario_name = "a-user-schedules-a-project-analysis"
    with add_scenario(scenario_name):
        e = get_entities()
        register(project, name="project")

        with add_goal("create a", e.project_analysis_job):
            with the(frontend).calls_the(create_project_analysis_job_api_view):
                with the(create_project_analysis_job_api_view).calls_the(
                    create_project_analysis_job_action
                ):
                    with the(create_project_analysis_job_action).creates_the(
                        e.project_analysis_job
                    ):
                        project_analysis_job_(e)

        with add_step("the", project_analysis_queue, "finds", e.jobs_to_run):
            jobs_to_run_(e)

        for idx, project_analysis_job in enumerate(e.jobs_to_run_.items):
            with the(project_analysis_queue).runs_the(
                f"{ith(idx)}", project_analysis_job
            ):
                with add_goal(
                    "create a", e.project_analysis, "from a", e.project_analysis_job
                ):
                    with the(project_analysis_queue).calls_the(
                        create_project_analysis_action
                    ):
                        with the(create_project_analysis_action).creates_a(
                            e.project_analysis
                        ):
                            e.project_analysis_job.project_analyses.append(
                                project_analysis_(e)
                            )

                        with (
                            the(create_project_analysis_action)
                            .gets_the(e.project_analysis.project)
                            .at_the_now_ts_of_the(e.project_analysis)
                        ):
                            project_at_now_()

                        with the(
                            create_project_analysis_action
                        ).loops_over_all_plots_in_the(e.project_at_now):
                            plot_list = get_project_plot_list_by_name(
                                e.project_at_now, "default"
                            )
                            for plot in plot_list.plots:
                                with add_goal(
                                    "add a",
                                    e.plot_analysis,
                                    "for the",
                                    plot,
                                    "to the",
                                    e.project_analysis,
                                ):
                                    with the(
                                        create_project_analysis_action
                                    ).creates_the(e.plot_analysis):
                                        e.project_analysis.plot_analyses.append(
                                            plot_analysis_(e, plot)
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
                    with the(e.project_analysis_queue).calls_the(
                        run_project_analysis_action
                    ):
                        for plot_analysis in e.project_analysis.plot_analyses:
                            with (
                                the(run_project_analysis_action)
                                .calls_the(run_plot_analysis_action)
                                .with_the(plot_analysis)
                            ):
                                with (
                                    the(run_plot_analysis_action)
                                    .creates_the(e.calcium_plot_analysis_job)
                                    .for_the(e.plot_at_now)
                                ):
                                    plot_at_now_(plot_analysis)
                                    calcium_plot_analysis_job_(e)

            for idx, plot_analysis in enumerate(e.project_analysis.plot_analyses):
                # TODO: the_backend_processes_a_calcium_job_result(idx, plot_analysis)
                pass

    return get_scenario(scenario_name)


def calcium_plot_analysis_job_(e):
    calcium_plot_analysis_job = register(
        CalciumPlotAnalysisJob(
            id=e.plot_analysis.id,
            polygon=e.plot_at_now.polygon,
        ),
        e.calcium_plot_analysis_job,
    )

    return calcium_plot_analysis_job


def plot_at_now_(plot_analysis):
    plot_at_now = register(
        at_ts(plot_analysis.plot, plot_analysis.now),
        name="plot_at_now",
    )

    return plot_at_now


def plot_analysis_(e, plot):
    register(
        PlotAnalyses.Models.PlotAnalysis(
            plot=plot,
            project_analysis=project_analysis,
            now=project_analysis.now,
            status=PlotAnalyses.Enums.PlotAnalysisStatus.RUNNING,
        ),
        e.plot_analysis,
    )


def project_at_now_():
    register(
        at_ts(project_analysis.project, project_analysis.now),
        name="project_at_now",
    )


def project_analysis_(e):
    register(
        ProjectAnalyses.Models.ProjectAnalysis(
            job=e.project_analysis_job,
            project=e.project_analysis_job.project,
            now=e.project_analysis_job.scheduled_at,
            status=ProjectAnalyses.Enums.ProjectAnalysisStatus.RUNNING,
        ),
        e.project_analysis,
    )


def jobs_to_run_(e):
    register(
        List(name="jobs_to_run", items=[e.project_analysis_job]),
        e.jobs_to_run,
    )


def project_analysis_job_(e):
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
