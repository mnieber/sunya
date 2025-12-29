# Module: project_analyses

## ProjectAnalyses

```python
class ProjectAnalyses(DjangoModule):
    class Models:
        class ProjectAnalysis(Entity):
            now: datetime
            status: 'ProjectAnalyses.Enums.ProjectAnalysisStatus'
            project: FK[Projects.Models.Project]
            job: FK[ProjectAnalysisJobs.Models.ProjectAnalysisJob]

    class Enums:
        class ProjectAnalysisStatus(Enum):
            RUNNING: Any = 'running'
            COMPLETED: Any = 'completed'
            FAILED: Any = 'failed'

    class Actions:
        class CreateProjectAnalysis(Action):
            class Args:
                project_analysis_job: ProjectAnalysisJobs.Models.ProjectAnalysisJob

        class RunProjectAnalysis(Action):
            class Args:
                project_analysis: 'ProjectAnalyses.Models.ProjectAnalysis'

    class DomainEvents:
        class ProjectAnalysisCreated:
            pass
```

