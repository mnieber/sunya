import typing as T
from datetime import datetime, timedelta

if T.TYPE_CHECKING:
    pass

from landler.backend.modules.projects import Projects
from landler.backend.app import Action, ApiView, Module
from sunya import Entity, MemField, actor_to_str, extend


class ProjectAnalysisJobs(Module):
    class Models:
        class ProjectAnalysisJob(Entity):
            project: Projects.Models.Project
            scheduled_at: datetime
            repeats_every: T.Optional[timedelta] = None
            is_active: bool = True

        class ProjectAnalysisQueue(Entity):
            project_analysis_jobs: list[
                "ProjectAnalysisJobs.Models.ProjectAnalysisJob"
            ] = []

    class Actions:
        class CreateProjectAnalysisJob(Action):
            class Args:
                project: Projects.Models.Project

    class Api:
        class CreateProjectAnalysisJob(ApiView):
            pass

    class DomainEvents:
        class ProjectAnalysisJobCreated:
            pass


create_project_analysis_job_action = (
    ProjectAnalysisJobs.Actions.CreateProjectAnalysisJob()
)
create_project_analysis_job_api_view = (
    ProjectAnalysisJobs.Api.CreateProjectAnalysisJob()
)

project_analysis_queue = ProjectAnalysisJobs.Models.ProjectAnalysisQueue()


@actor_to_str.method((ProjectAnalysisJobs.Models.ProjectAnalysisJob,))
def project_analysis_job_to_str(project_analysis_job):
    return f"{project_analysis_job.project.name}+:project-analysis-job"


@actor_to_str.method((ProjectAnalysisJobs.Models.ProjectAnalysisQueue,))
def project_analysis_queue_to_str(project_analysis_queue):
    return f":project-analysis-queue"


@extend(ProjectAnalysisJobs.Models.ProjectAnalysisJob)
class ExtendProjectAnalysisJob:
    project_analyses = MemField(lambda: list())
