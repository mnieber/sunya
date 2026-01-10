# Module: project_analysis_jobs

## ProjectAnalysisJobs

```python
class ProjectAnalysisJobs(DjangoModule):
    class Models:
        class ProjectAnalysisJob(Entity):
            scheduled_at: datetime
            repeats_every: T.Optional[timedelta] = None
            is_active: bool = True
            project: FK[Projects.Models.Project]
            project_analyses: RelatedSet['ProjectAnalyses.Models.ProjectAnalysis'] = []

        class ProjectAnalysisQueue(Entity):
            project_analysis_jobs: RelatedSet['ProjectAnalysisJobs.Models.ProjectAnalysisJob'] = []

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
```

