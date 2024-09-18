import landler.backend.namespace as B
import landler.stack.namespace as S
from default.stack.namespace import List
from landler.stack.namespace import ith, at_ts
from sunya import (
    add_goal,
    add_scenario,
    run_scenario,
    add_step,
    add_actor,
    get_scenario,
    add_role,
    the,
    G as g,
)

from sunya.utils import get_time


scenario_name = "backend/ms4-a-user-schedules-a-project-analysis"


def start(a_project, variation="default"):
    project = add_role("Project")
    project_analysis_job = add_role("ProjectAnalysisJob")
    jobs_to_run = add_role("JobsToRun")
    project_analysis = add_role("ProjectAnalysis")
    project_at_now = add_role("ProjectAtNow")
    plot_at_now = add_role("PlotAtNow")

    with add_scenario(scenario_name):
        project.actor = add_actor(a_project, name="project")

        with add_goal("create a", project_analysis_job):
            with the(g.create_project_analysis_job_api_view).calls_the(
                g.create_project_analysis_job_action
            ):
                with the(g.create_project_analysis_job_action).creates_the(
                    project_analysis_job
                ):
                    project_analysis_job_()

        with add_step("the", g.project_analysis_queue, "finds", jobs_to_run):
            jobs_to_run.actor = jobs_to_run_()

        for idx, a_project_analysis_job in enumerate(g.jobs_to_run.items):
            with the(g.project_analysis_queue).runs_the(
                f"{ith(idx)}", project_analysis_job
            ):
                project_analysis_job.actor = a_project_analysis_job

                with add_goal(
                    "create a", project_analysis, "from a", project_analysis_job
                ):
                    with the(g.project_analysis_queue).calls_the(
                        g.create_project_analysis_action
                    ):
                        with the(g.create_project_analysis_action).creates_a(
                            project_analysis
                        ):
                            a_project_analysis = project_analysis_(idx)
                            a_project_analysis_job.project_analyses.append(
                                a_project_analysis
                            )

                        with (
                            the(g.create_project_analysis_action)
                            .gets_the(project)
                            .at_the_now_ts_of_the(project_analysis)
                        ):
                            a_project_at_now = project_at_now_()

                        with the(
                            g.create_project_analysis_action
                        ).loops_over_all_plots_in_the(project_at_now):
                            plot_list = B.get_project_plot_list_by_name(
                                a_project_at_now, "default"
                            )
                            for plot in plot_list.plots:
                                with add_goal(
                                    "add a",
                                    plot_analysis,
                                    "for the",
                                    plot,
                                    "to the",
                                    project_analysis,
                                ):
                                    with the(
                                        g.create_project_analysis_action
                                    ).creates_the(plot_analysis):
                                        g.project_analysis.plot_analyses.append(
                                            plot_analysis_()
                                        )

                with add_goal(
                    "run each",
                    plot_analysis,
                    "in the",
                    project_analysis,
                    "for the",
                    plot,
                    "at the now timestamp of the",
                    plot_analysis,
                ):
                    with the(g.project_analysis_queue).calls_the(
                        g.run_project_analysis_action
                    ):
                        for plot_analysis in g.project_analysis.plot_analyses:
                            with (
                                the(g.run_project_analysis_action)
                                .calls_the(g.run_plot_analysis_action)
                                .with_the(plot_analysis)
                            ):
                                with (
                                    the(g.run_plot_analysis_action)
                                    .creates_the(g.calcium_plot_analysis_job)
                                    .for_the(plot_at_now)
                                ):
                                    plot_at_now_(e, plot_analysis)
                                    calcium_plot_analysis_job_()

            for idx, plot_analysis in enumerate(e.project_analysis.plot_analyses):
                # TODO: the_backend_processes_a_calcium_job_result(idx, plot_analysis)
                pass

    return get_scenario(scenario_name)


def calcium_plot_analysis_job_():
    unadd_actor("calcium_plot_analysis_job")
    calcium_plot_analysis_job = add_actor(
        S.CalciumPlotAnalysisJob(
            id=e.plot_analysis.id,
            polygon=e.plot_at_now.polygon,
        ),
        e.calcium_plot_analysis_job,
    )

    return calcium_plot_analysis_job


def plot_at_now_(e, plot_analysis):
    unadd_actor("plot_at_now")
    return add_actor(
        at_ts(plot_analysis.plot, plot_analysis.now),
        e.plot_at_now,
    )


def plot_analysis_(e, plot):
    unadd_actor("plot_analysis")
    return add_actor(
        B.PlotAnalyses.Models.PlotAnalysis(
            plot=plot,
            project_analysis=e.project_analysis,
            now=e.project_analysis.now,
            status=B.PlotAnalyses.Enums.PlotAnalysisStatus.RUNNING,
        ),
        e.plot_analysis,
    )


def project_at_now_():
    unadd_actor("project_at_now")
    return add_actor(
        at_ts(e.project_analysis.project, e.project_analysis.now),
        e.project_at_now,
    )


def project_analysis_(idx):
    return add_actor(
        B.ProjectAnalyses.Models.ProjectAnalysis(
            job=e.project_analysis_job,
            project=e.project_analysis_job.project,
            now=e.project_analysis_job.scheduled_at,
            status=B.ProjectAnalyses.Enums.ProjectAnalysisStatus.RUNNING,
        ),
        name=f"project_analysis_{idx}",
    )


def jobs_to_run_():
    return add_actor(
        List(name="jobs_to_run", items=[g.project_analysis_job]), name="jobs_to_run"
    )


def project_analysis_job_():
    return add_actor(
        B.ProjectAnalysisJobs.Models.ProjectAnalysisJob(
            project=e.project,
            scheduled_at=get_time.now(bump=True),
        ),
        e.project_analysis_job,
    )


def run():
    from . import ms3_a_user_adds_a_plot_to_a_project

    ms3_scenario = run_scenario(ms3_a_user_adds_a_plot_to_a_project)
    project = ms3_scenario.get_entity_by_name("project")

    return start(a_project=project)


if __name__ == "__main__":
    run()
