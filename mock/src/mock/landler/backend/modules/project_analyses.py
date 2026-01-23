import typing as T
from datetime import datetime

if T.TYPE_CHECKING:
    pass

from mock.landler.backend.modules.project_analysis_jobs import ProjectAnalysisJobs
from mock.landler.backend.modules.projects import Projects
from mock.entities.python_app.namespace import Enum
from mock.entities.django_app.namespace import Action, DjangoModule

from sunya import Entity, FK


class ProjectAnalyses(DjangoModule):
    class Models:
        class ProjectAnalysis(Entity):
            """A Django model that contains a project analysis.

            The project analysis will consider all historical data that
            was created up to the `now` timestamp. Note that this considers
            how old/new the historical data is, not how early/late it is.

            Also note that this implies a race condition, because a previous project
            analysis may nor may not finish (and add more historical data)
            before this one starts. This is a design decision: we generally don't wait
            for other project analyses to finish before starting a new one. The
            exception is when a previous project analysis on the same project (and
            product) is still running. In that case, we wait.
            """

            now: datetime
            status: "ProjectAnalyses.Enums.ProjectAnalysisStatus"
            project: FK[Projects.Models.Project]
            job: FK[ProjectAnalysisJobs.Models.ProjectAnalysisJob]

    class Enums:
        class ProjectAnalysisStatus(Enum):
            RUNNING = "running"
            COMPLETED = "completed"
            FAILED = "failed"

    class Actions:
        class CreateProjectAnalysis(Action):
            class Args:
                project_analysis_job: ProjectAnalysisJobs.Models.ProjectAnalysisJob

        class RunProjectAnalysis(Action):
            class Args:
                project_analysis: "ProjectAnalyses.Models.ProjectAnalysis"

    class DomainEvents:
        class ProjectAnalysisCreated:
            pass
