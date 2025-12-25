from sunya import MemField, extend
from . import namespace as B


@extend(B.ProjectAnalyses.Models.ProjectAnalysis)
class ExtendProjectAnalysis:
    plot_analyses = MemField(lambda: list())


@extend(B.Projects.Models.Project)
class ExtendProject:
    plot_lists = MemField(lambda: list())


@extend(B.ProjectAnalysisJobs.Models.ProjectAnalysisJob)
class ExtendProjectAnalysisJob:
    project_analyses = MemField(lambda: list())
