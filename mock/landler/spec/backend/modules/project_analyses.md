1 Models

1.1 Model: ProjectAnalysis

id: UUID
project: Project
job: ProjectAnalysisJob
now: datetime
status: ProjectAnalysisStatus

2 Enums

2.1 Enum: ProjectAnalysisStatus

Items:
running
completed
failed

3 Actions

3.1 Action: create_project_analysis

Arguments:
project_analysis_job: ProjectAnalysisJob

3.2 Action: run_project_analysis

Arguments:
project_analysis: ProjectAnalysis

4 Api views

