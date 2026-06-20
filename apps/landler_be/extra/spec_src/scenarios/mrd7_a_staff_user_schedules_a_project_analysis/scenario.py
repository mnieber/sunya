import sunya
from sunya import M as m
from sunya import R as r
from sunya import goal, it, the

scenario = sunya.add_scenario(f"MRD7: A staff user schedules a project analysis")


def run_scenario():
    r.user = m.External.Actors.User
    r.frontend = m.External.Actors.Frontend
    r.create_project_analysis_job_api_view = m.ProjectAnalyses.ApiViews.CreateProjectAnalysisJobApiView
    r.create_project_analysis_job_action = m.ProjectAnalyses.Actions.CreateProjectAnalysisJob
    r.project_analysis_queue = m.ProjectAnalyses.ProjectAnalysisQueue
    r.create_project_analysis_action = m.ProjectAnalyses.Actions.CreateProjectAnalysis
    r.run_project_analysis_action = m.ProjectAnalyses.Actions.RunProjectAnalysis
    r.run_plot_analysis_action = m.PlotAnalyses.Actions.RunPlotAnalysis

    with goal().create_a(r.project_analysis_job):
        # Create a project analysis job
        with the(r.frontend).calls(r.create_project_analysis_job_api_view):
            with it().calls(r.create_project_analysis_job_action):
                it().creates(r.project_analysis_job)
                it().adds(r.project_analysis_job).to_the(r.project_analysis_queue)

    with goal().run_the(r.project_analysis_jobs):
        # Find project analysis jobs to run
        with the(r.project_analysis_queue).finds_the(r.jobs_to_run):
            pass

        # Run each project analysis job
        with the(r.project_analysis_queue).runs_each(r.project_analysis_job):
            # Create project analysis
            with it().calls(r.create_project_analysis_action):
                it().creates(r.project_analysis).with_status_running()
                it().determines_the(r.project_at_now).based_on_the_now_timestamp()
                it().finds_the(r.default_plot_list).for_the(r.project_at_now)

                # Create plot analysis for each plot
                with it().loops_over_all_plots_in_the(r.project_at_now):
                    it().creates(r.plot_analysis).for_each(r.plot)
                    it().adds(r.plot_analysis).to_the(r.project_analysis)

            # Run all plot analyses
            with it().calls(r.run_project_analysis_action):
                with it().runs_each(r.plot_analysis):
                    with it().calls(r.run_plot_analysis_action).for_each(r.plot_analysis):
                        it().determines_the(r.plot_at_now).based_on_the_now_timestamp()
                        it().creates_the(r.calcium_plot_analysis_job)


markdown_node = sunya.add_markdown_node(scenario, "A staff user schedules a project analysis")

markdown_node.markdown = """
A staff user schedules a project analysis job. The system creates the job, adds it to the queue, and then processes it by creating a project analysis with plot analyses for each plot in the project. This scenario demonstrates how temporal snapshots of projects and plots are created for analysis.

### Steps

#### It creates the project analysis job

The frontend calls the create project analysis job API view.</br>
The API view calls the `CreateProjectAnalysisJob` action.</br>
The action creates the project analysis job and adds it to the project analysis queue.</br>

**Note [1]**: The project analysis job is added to the queue where it waits to be processed. The queue ensures that jobs are processed in order and that multiple jobs can be queued for later processing.</br>

#### It processes the project analysis job

The project analysis queue finds all jobs to run.</br>
For each job, the queue calls `CreateProjectAnalysis` to create the project analysis with status "RUNNING".</br>

**Note [2]**: The project analysis has a "now" timestamp that represents the point in time for which the analysis is being performed. This allows the system to create temporal snapshots of the project state.</br>

The action determines the project state at the analysis timestamp (project at now).</br>

**Note [3]**: The project_at_now represents the project's state at the "now" timestamp. The project_at_now._now_ field matches the project_analysis.now timestamp, ensuring consistency.</br>

The action finds the default plot list for the project.</br>

**Note [4]**: For each plot in the default plot list, a plot analysis is created. Each plot analysis inherits the same "now" timestamp from its parent project analysis, ensuring all plots are analyzed at the same point in time.</br>

For each plot in the list, the action creates a plot analysis with status "RUNNING" and adds it to the project analysis.</br>

**Note [5]**: The plot_analysis.now timestamp equals the project_analysis.now timestamp. The plot_analysis.status is set to "RUNNING" to indicate that the analysis is in progress.</br>

#### It runs the plot analyses

The queue calls `RunProjectAnalysis` to run all plot analyses.</br>
For each plot analysis, the action calls `RunPlotAnalysis`.</br>

**Note [6]**: Similar to project_at_now, plot_at_now represents the plot's state at the analysis timestamp. The plot_at_now._now_ field matches the plot_analysis.now timestamp.</br>

The action determines the plot state at the analysis timestamp (plot at now).</br>

**Note [7]**: The calcium plot analysis job is created using the polygon from plot_at_now. This ensures that the analysis uses the plot's geometry as it existed at the specified timestamp. The calcium_plot_analysis_job.polygon field equals plot_at_now.polygon.</br>

The action creates a calcium plot analysis job for the plot.</br>

**Note [8] (TODO)**: The processing of calcium job results is not yet implemented in this scenario. Future work will include handling the results returned by the calcium analysis engine and updating the plot analysis status accordingly.</br>

### Diagram

```mermaid
sequenceDiagram
    actor User
    participant Frontend as Frontend
    participant CreateProjectAnalysisJobApiView as CreateProjectAnalysisJobApiView
    participant CreateProjectAnalysisJob as CreateProjectAnalysisJob (action)
    participant ProjectAnalysisQueue as ProjectAnalysisQueue
    participant CreateProjectAnalysis as CreateProjectAnalysis (action)
    participant RunProjectAnalysis as RunProjectAnalysis (action)
    participant RunPlotAnalysis as RunPlotAnalysis (action)

    Note over Frontend,CreateProjectAnalysisJob: Create Project Analysis Job
    User->>Frontend: schedule project analysis
    Frontend->>CreateProjectAnalysisJobApiView: calls
    CreateProjectAnalysisJobApiView->>CreateProjectAnalysisJob: create_project_analysis_job()
    CreateProjectAnalysisJob->>CreateProjectAnalysisJob: create project analysis job
    Note over CreateProjectAnalysisJob: See [1]
    CreateProjectAnalysisJob->>ProjectAnalysisQueue: add job to queue
    CreateProjectAnalysisJob-->>CreateProjectAnalysisJobApiView: project_analysis_job

    Note over ProjectAnalysisQueue,CreateProjectAnalysis: Process Job
    ProjectAnalysisQueue->>ProjectAnalysisQueue: find jobs to run

    loop for each job
        Note over ProjectAnalysisQueue: See [2]
        ProjectAnalysisQueue->>CreateProjectAnalysis: create_project_analysis(job)
        CreateProjectAnalysis->>CreateProjectAnalysis: create project analysis with status RUNNING

        Note over CreateProjectAnalysis: See [3]
        CreateProjectAnalysis->>CreateProjectAnalysis: determine project at now (project state at timestamp)

        CreateProjectAnalysis->>CreateProjectAnalysis: find default plot list

        Note over CreateProjectAnalysis: See [4, 5]
        loop for each plot
            CreateProjectAnalysis->>CreateProjectAnalysis: create plot analysis with status RUNNING
            CreateProjectAnalysis->>CreateProjectAnalysis: add plot analysis to project analysis
        end

        ProjectAnalysisQueue->>RunProjectAnalysis: run_project_analysis(project_analysis)

        loop for each plot analysis
            Note over RunProjectAnalysis: See [6]
            RunProjectAnalysis->>RunPlotAnalysis: run_plot_analysis(plot_analysis)
            RunPlotAnalysis->>RunPlotAnalysis: determine plot at now (plot state at timestamp)

            Note over RunPlotAnalysis: See [7]
            RunPlotAnalysis->>RunPlotAnalysis: create calcium plot analysis job (using polygon from plot_at_now)
        end

        Note over ProjectAnalysisQueue: See [8] (TODO)
        Note over ProjectAnalysisQueue: Future: process calcium job results
    end
```
"""
