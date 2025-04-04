import typing as T
from datetime import datetime
from kits.django_app.namespace import DjangoModule

if T.TYPE_CHECKING:
    pass


from mock.landler.backend.modules.plots import Plots
from mock.landler.backend.modules.project_analyses import ProjectAnalyses
from kits.python_app.namespace import Enum
from kits.django_app.namespace import Action
from sunya import Entity, FK


class PlotAnalyses(DjangoModule):
    class Models:
        class PlotAnalysis(Entity):
            now: datetime
            status: "PlotAnalyses.Enums.PlotAnalysisStatus"
            plot: FK[Plots.Models.Plot]
            project_analysis: FK[ProjectAnalyses.Models.ProjectAnalysis]

    class Enums:
        class PlotAnalysisStatus(Enum):
            RUNNING = "running"
            COMPLETED = "completed"
            FAILED = "failed"

    class Actions:
        class CreatePlotAnalysis(Action):
            class Args:
                project_analysis: ProjectAnalyses.Models.ProjectAnalysis

        class RunPlotAnalysis(Action):
            class Args:
                project_analysis: ProjectAnalyses.Models.ProjectAnalysis

    class DomainEvents:
        class PlotAnalysisCreated:
            pass
