from domain.app import *
from domain.datatypes import *
from sunya import (
    List,
    add_scenario,
    add_step,
    get_entity,
    get_scenario,
    preregister,
    register,
)

from .the_backend_processes_a_calcium_job_result import (
    the_backend_processes_a_calcium_job_result,
)
from .the_create_project_analysis_job_api_view_creates_a_project_analysis_job import (
    the_create_project_analysis_job_api_view_creates_a_project_analysis_job,
)
from .the_project_analysis_queue_calls_the_create_project_analysis_action import (
    the_project_analysis_queue_calls_the_create_project_analysis_action,
)
from .the_project_analysis_queue_calls_the_run_project_analysis_action import (
    the_project_analysis_queue_calls_the_run_project_analysis_action,
)


def start(project, variation="default"):
    scenario_name = "a-user-schedules-a-project-analysis"
    with add_scenario(scenario_name):
        p_project_analysis_job = preregister("project_analysis_job")
        with the_fe_posts_to_create_a_project_analysis_job(p_project_analysis_job):
            new_project_analysis_job = (
                the_create_project_analysis_job_api_view_creates_a_project_analysis_job(
                    p_project_analysis_job, project
                )
            )

        p_jobs_to_run = preregister("jobs_to_run")
        with the_project_analysis_queue_finds_jobs_to_run_next(p_jobs_to_run):
            jobs_to_run = register(
                List(name="jobs_to_run", items=[new_project_analysis_job]),
                p_jobs_to_run,
            )

        for idx, project_analysis_job in enumerate(jobs_to_run.items):
            with the_project_analysis_queue_runs_the_project_analysis_job(
                idx, project_analysis_job
            ):
                project_analysis = (
                    the_project_analysis_queue_calls_the_create_project_analysis_action(
                        project_analysis_job
                    )
                )
                the_project_analysis_queue_calls_the_run_project_analysis_action(
                    project_analysis
                )

            for idx, plot_analysis in enumerate(project_analysis.plot_analyses):
                the_backend_processes_a_calcium_job_result(idx, plot_analysis)

    return get_scenario(scenario_name)


def the_fe_posts_to_create_a_project_analysis_job(p_project_analysis_job):
    return add_step(
        "the",
        frontend,
        "call the",
        create_project_analysis_job_api_view,
        "to create a",
        p_project_analysis_job,
    )


def the_project_analysis_queue_runs_the_project_analysis_job(idx, project_analysis_job):
    return add_step(
        "the",
        project_analysis_queue,
        f"runs the {ith(idx)}",
        project_analysis_job,
    )


def the_project_analysis_queue_finds_jobs_to_run_next(p_jobs_to_run):
    return add_step("the", project_analysis_queue, "finds", p_jobs_to_run)


def run():
    import domain.scenarios.s3_a_user_adds_a_plot_to_a_project

    domain.scenarios.s3_a_user_adds_a_plot_to_a_project.run()
    project = get_entity(Projects.Models.Project, name="my-project")

    return start(project=project)


if __name__ == "__main__":
    run()
