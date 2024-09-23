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
    get_scenario_name,
    add_role,
    the,
    G as g,
)

from sunya.utils import get_time


scenario_name = f"backend/{get_scenario_name(__file__)}"


def start(a_project, variation="default"):
    calcium_plot_analysis_job = add_role("CalciumPlotAnalysisJob")
    jobs_to_run = add_role("JobsToRun")
    plot_analysis = add_role("PlotAnalysis")
    plot_at_now = add_role("PlotAtNow")
    plot = add_role("Plot")
    project = add_role("Project")
    project_analysis = add_role("ProjectAnalysis")
    project_analysis_job = add_role("ProjectAnalysisJob")
    project_at_now = add_role("ProjectAtNow")

    with add_scenario(scenario_name):
        project.actor = add_actor(a_project, name="project")

        with add_goal("create a", project_analysis_job):
            get_time.now(bump=True)

            with the(g.create_project_analysis_job_api_view).calls_the(
                g.create_project_analysis_job_action
            ):
                with the(g.create_project_analysis_job_action).creates_the(
                    project_analysis_job
                ):
                    project_analysis_job.actor = project_analysis_job_(project.actor)

        with add_step("the", g.project_analysis_queue, "finds", jobs_to_run):
            jobs_to_run.actor = jobs_to_run_(project_analysis_job.actor)

        for idx, a_project_analysis_job in enumerate(jobs_to_run.actor.items):
            project_analysis_job.actor = a_project_analysis_job

            with the(g.project_analysis_queue).runs_the(
                f"{ith(idx)}", project_analysis_job
            ):
                with add_goal(
                    "create a", project_analysis, "from a", project_analysis_job
                ):
                    with the(g.project_analysis_queue).calls_the(
                        g.create_project_analysis_action
                    ):
                        with the(g.create_project_analysis_action).creates_a(
                            project_analysis
                        ):
                            project_analysis.actor = project_analysis_(
                                project_analysis_job.actor, idx
                            )
                            project_analysis_job.actor.project_analyses.append(
                                project_analysis.actor
                            )

                        with (
                            the(g.create_project_analysis_action)
                            .determines_the(project_at_now)
                            .as_the(project)
                            .at_the_now_ts_of_the(project_analysis)
                        ):
                            project_at_now.actor = project_at_now_(
                                project_analysis.actor, idx
                            )

                        with the(
                            g.create_project_analysis_action
                        ).loops_over_all_plots_in_the(project_at_now):
                            plot_list = B.get_project_plot_list_by_name(
                                project_at_now.actor, "default"
                            )
                            for idx, a_plot in enumerate(plot_list.plots):
                                plot.actor = a_plot

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
                                        plot_analysis.actor = plot_analysis_(
                                            plot.actor, project_analysis.actor, idx
                                        )
                                        project_analysis.actor.plot_analyses.append(
                                            plot_analysis.actor
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
                        for idx, a_plot_analysis in enumerate(
                            project_analysis.actor.plot_analyses
                        ):
                            plot_analysis.actor = a_plot_analysis

                            with (
                                the(g.run_project_analysis_action)
                                .calls_the(g.run_plot_analysis_action)
                                .with_the(plot_analysis)
                            ):
                                with (
                                    the(g.run_plot_analysis_action)
                                    .creates_the(calcium_plot_analysis_job)
                                    .for_the(plot_at_now)
                                ):
                                    plot_at_now.actor = plot_at_now_(
                                        plot_analysis.actor, idx
                                    )
                                    calcium_plot_analysis_job.actor = (
                                        calcium_plot_analysis_job_(
                                            plot_analysis.actor, plot_at_now.actor, idx
                                        )
                                    )

            for idx, plot_analysis in enumerate(project_analysis.actor.plot_analyses):
                # TODO: the_backend_processes_a_calcium_job_result(plot_analysis, idx)
                pass

    return get_scenario(scenario_name)


def calcium_plot_analysis_job_(a_plot_analysis, a_plot_at_now, idx):
    return add_actor(
        S.CalciumPlotAnalysisJob(
            id=a_plot_analysis.id,
            polygon=a_plot_at_now.polygon,
        ),
        name=f"calcium_plot_analysis_job_{idx}",
    )


def plot_at_now_(a_plot_analysis, idx):
    return add_actor(
        at_ts(a_plot_analysis.plot, a_plot_analysis.now),
        name=f"plot_at_now_{idx}",
    )


def plot_analysis_(a_plot, a_project_analysis, idx):
    return add_actor(
        B.PlotAnalyses.Models.PlotAnalysis(
            plot=a_plot,
            project_analysis=a_project_analysis,
            now=a_project_analysis.now,
            status=B.PlotAnalyses.Enums.PlotAnalysisStatus.RUNNING,
        ),
        name=f"plot_analysis_{idx}",
    )


def project_at_now_(a_project_analysis, idx):
    return add_actor(
        at_ts(a_project_analysis.project, a_project_analysis.now),
        f"project_at_now_{idx}",
    )


def project_analysis_(a_project_analysis_job, idx):
    return add_actor(
        B.ProjectAnalyses.Models.ProjectAnalysis(
            job=a_project_analysis_job,
            project=a_project_analysis_job.project,
            now=a_project_analysis_job.scheduled_at,
            status=B.ProjectAnalyses.Enums.ProjectAnalysisStatus.RUNNING,
        ),
        name=f"project_analysis_{idx}",
    )


def jobs_to_run_(a_project_analysis_job):
    return add_actor(
        List(name="jobs_to_run", items=[a_project_analysis_job]), name="jobs_to_run"
    )


def project_analysis_job_(a_project):
    return add_actor(
        B.ProjectAnalysisJobs.Models.ProjectAnalysisJob(
            project=a_project,
            scheduled_at=get_time.now(bump=True),
        ),
        "project_analysis_job",
    )


def run():
    from . import mrd5_a_user_adds_a_plot_to_a_project

    ms3_scenario = run_scenario(mrd5_a_user_adds_a_plot_to_a_project)
    project = ms3_scenario.get_entity_by_name("project")

    return start(a_project=project)


if __name__ == "__main__":
    run()
