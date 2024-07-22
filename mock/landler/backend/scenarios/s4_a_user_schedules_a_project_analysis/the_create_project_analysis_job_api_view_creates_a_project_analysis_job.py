from landler.backend.app import *
from sunya import add_step, register


def the_create_project_analysis_job_api_view_creates_a_project_analysis_job(
    p_project_analysis_job, project
):
    with add_step(
        "The",
        create_project_analysis_job_api_view,
        "calls the",
        create_project_analysis_job_action,
        "to create a",
        p_project_analysis_job,
    ):
        with add_step(
            "The",
            create_project_analysis_job_action,
            "creates the",
            p_project_analysis_job,
        ):
            project_analysis_job = register(
                ProjectAnalysisJobs.Models.ProjectAnalysisJob(
                    project=project,
                    scheduled_at=datetime.now(),
                ),
                p_project_analysis_job,
            )

    return project_analysis_job
