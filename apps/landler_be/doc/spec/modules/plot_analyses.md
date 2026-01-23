# Module: plot_analyses

## PlotAnalyses

```python
class PlotAnalyses(DjangoModule):
    class Models:
        class PlotAnalysis(Entity):
            now: datetime
            status: 'PlotAnalyses.Enums.PlotAnalysisStatus'
            plot: FK[Plots.Models.Plot]
            project_analysis: FK[ProjectAnalyses.Models.ProjectAnalysis]

    class Enums:
        class PlotAnalysisStatus(Enum):
            RUNNING: Any = 'running'
            COMPLETED: Any = 'completed'
            FAILED: Any = 'failed'

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
```

