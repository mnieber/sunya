import landler.backend.namespace as B
import landler.stack.namespace as S
from landler.stack.namespace import ith, at_ts
from sunya import (
    add_goal,
    add_scenario,
    add_step,
    get_entities,
    get_scenario,
    List,
    register,
    the,
    maybe_name,
    G as g,
)

from sunya.utils import get_time


def start(project, variation="default"):
    scenario_name = "a-user-schedules-a-project-analysis"
    with add_scenario(scenario_name):
        e = get_entities()
        register(project, name="project")

        with add_goal("create a", e.project_analysis_job):
            with the(g.frontend).calls_the(g.create_project_analysis_job_api_view):
                with the(g.create_project_analysis_job_api_view).calls_the(
                    g.create_project_analysis_job_action
                ):
                    with the(g.create_project_analysis_job_action).creates_the(
                        e.project_analysis_job
                    ):
                        project_analysis_job_(e)

        with add_step("the", g.project_analysis_queue, "finds", e.jobs_to_run):
            jobs_to_run_(e)

        for idx, project_analysis_job in enumerate(e.jobs_to_run.items):
            with the(g.project_analysis_queue).runs_the(
                f"{ith(idx)}", project_analysis_job
            ):
                with add_goal(
                    "create a", e.project_analysis, "from a", e.project_analysis_job
                ):
                    with the(g.project_analysis_queue).calls_the(
                        g.create_project_analysis_action
                    ):
                        with the(g.create_project_analysis_action).creates_a(
                            e.project_analysis
                        ):
                            e.project_analysis_job.project_analyses.append(
                                project_analysis_(e)
                            )

                        with (
                            the(g.create_project_analysis_action)
                            .gets_the(e.project_analysis.project)
                            .at_the_now_ts_of_the(e.project_analysis)
                        ):
                            project_at_now_(e)

                        with the(
                            g.create_project_analysis_action
                        ).loops_over_all_plots_in_the(e.project_at_now):
                            plot_list = B.get_project_plot_list_by_name(
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
                                        g.create_project_analysis_action
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
                        g.run_project_analysis_action
                    ):
                        for plot_analysis in e.project_analysis.plot_analyses:
                            with (
                                the(g.run_project_analysis_action)
                                .calls_the(g.run_plot_analysis_action)
                                .with_the(plot_analysis)
                            ):
                                with (
                                    the(g.run_plot_analysis_action)
                                    .creates_the(e.calcium_plot_analysis_job)
                                    .for_the(e.plot_at_now)
                                ):
                                    plot_at_now_(e, plot_analysis)
                                    calcium_plot_analysis_job_(e)

            for idx, plot_analysis in enumerate(e.project_analysis.plot_analyses):
                # TODO: the_backend_processes_a_calcium_job_result(idx, plot_analysis)
                pass

    return get_scenario(scenario_name)


def calcium_plot_analysis_job_(e):
    calcium_plot_analysis_job = register(
        S.CalciumPlotAnalysisJob(
            id=e.plot_analysis.id,
            polygon=e.plot_at_now.polygon,
        ),
        **maybe_name(e.calcium_plot_analysis_job, "calcium_plot_analysis_job"),
    )

    return calcium_plot_analysis_job


def plot_at_now_(e, plot_analysis):
    return register(
        at_ts(plot_analysis.plot, plot_analysis.now),
        **maybe_name(e.plot_at_now, "plot_at_now"),
    )


def plot_analysis_(e, plot):
    return register(
        B.PlotAnalyses.Models.PlotAnalysis(
            plot=plot,
            project_analysis=e.project_analysis,
            now=e.project_analysis.now,
            status=B.PlotAnalyses.Enums.PlotAnalysisStatus.RUNNING,
        ),
        **maybe_name(e.plot_analysis, "plot_analysis"),
    )


def project_at_now_(e):
    return register(
        at_ts(e.project_analysis.project, e.project_analysis.now),
        **maybe_name(e.project_at_now, "project_at_now"),
    )


def project_analysis_(e):
    return register(
        B.ProjectAnalyses.Models.ProjectAnalysis(
            job=e.project_analysis_job,
            project=e.project_analysis_job.project,
            now=e.project_analysis_job.scheduled_at,
            status=B.ProjectAnalyses.Enums.ProjectAnalysisStatus.RUNNING,
        ),
        **maybe_name(e.project_analysis, "project_analysis"),
    )


def jobs_to_run_(e):
    return register(
        List(name="jobs_to_run", items=[e.project_analysis_job]),
        e.jobs_to_run,
    )


def project_analysis_job_(e):
    return register(
        B.ProjectAnalysisJobs.Models.ProjectAnalysisJob(
            project=e.project,
            scheduled_at=get_time.now(bump=True),
        ),
        e.project_analysis_job,
    )


def run():
    import landler.backend.scenarios.ms3_a_user_adds_a_plot_to_a_project

    ms3_scenario = landler.backend.scenarios.ms3_a_user_adds_a_plot_to_a_project.run()
    project = ms3_scenario.get_entity_by_name("project")

    return start(project=project)


if __name__ == "__main__":
    run()
