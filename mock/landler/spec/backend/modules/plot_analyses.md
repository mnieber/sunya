1 Models

1.1 Model: PlotAnalysis

id: UUID
plot: Plot
project_analysis: ProjectAnalysis
now: datetime
status: PlotAnalysisStatus

2 Enums

2.1 Enum: PlotAnalysisStatus

Items:
running
completed
failed

3 Actions

3.1 Action: create_plot_analysis

Arguments:
project_analysis: ProjectAnalysis

3.2 Action: run_plot_analysis

Arguments:
project_analysis: ProjectAnalysis

4 Api views

