import typing as T
from datetime import datetime

if T.TYPE_CHECKING:
    pass


from landler.backend.modules.plots import Plots
from landler.backend.modules.project_analyses import ProjectAnalyses
from default.stack.namespace import Module, Enum
from default.backend.namespace import Action
from sunya import EntityWithId, MemField, actor_to_str, extend, G as g


class PlotAnalyses(Module):
    class Models:
        class PlotAnalysis(EntityWithId):
            plot: Plots.Models.Plot
            project_analysis: ProjectAnalyses.Models.ProjectAnalysis
            now: datetime
            status: "PlotAnalyses.Enums.PlotAnalysisStatus"

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


g.create_plot_analysis_action = PlotAnalyses.Actions.CreatePlotAnalysis()
g.run_plot_analysis_action = PlotAnalyses.Actions.RunPlotAnalysis()


@actor_to_str.method((PlotAnalyses.Models.PlotAnalysis,))
def plot_analysis_to_str(plot_analysis):
    return f"{plot_analysis.plot.name}@{plot_analysis.now}+:plot-analysis"


@extend(ProjectAnalyses.Models.ProjectAnalysis)
class ExtendProjectAnalysis:
    plot_analyses = MemField(lambda: list())
