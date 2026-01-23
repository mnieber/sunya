import typing as T
from datetime import datetime, timedelta

if T.TYPE_CHECKING:
    from .project_analyses import ProjectAnalyses

from mock.landler.backend.modules.projects import Projects
from mock.entities.django_app.namespace import Action, ApiView, DjangoModule

from sunya import Entity, RelatedSet, FK


class ProjectAnalysisJobs(DjangoModule):
    class Models:
        class ProjectAnalysisJob(Entity):
            """
            From this model, ProjectAnalyses are created (if is_active).
            If repeats_every is not None, then multiple ProjectAnalyses will be created,
            each with a scheduled_at that is scheduled_at + repeats_every.
            """

            scheduled_at: datetime
            repeats_every: T.Optional[timedelta] = None
            is_active: bool = True
            project: FK[Projects.Models.Project]
            project_analyses: RelatedSet["ProjectAnalyses.Models.ProjectAnalysis"] = []

        class ProjectAnalysisQueue(Entity):
            project_analysis_jobs: RelatedSet[
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
