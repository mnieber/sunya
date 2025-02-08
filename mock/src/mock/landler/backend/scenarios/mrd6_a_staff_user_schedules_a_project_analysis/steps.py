import mock.landler.backend.namespace as B
import mock.landler.stack.namespace as S
from sunya import R as r, G as g, match_step as match, it
from datetime import datetime
import copy


def implement_step(step):
    # create project analysis job
    if match(
        step,
        it()
        .creates_a(r.project_analysis_job)
        .and_adds_it_to_the(g.project_analysis_queue),
    ):
        r.project_analysis_job = B.ProjectAnalysisJobs.Models.ProjectAnalysisJob(
            scheduled_at=datetime.now(), is_active=True, project=r.project
        )
        g.project_analysis_queue.project_analysis_jobs.append(r.project_analysis_job)
        r.jobs_to_run = g.project_analysis_queue.project_analysis_jobs

    # create project analysis
    elif match(
        step,
        it().creates_a(r.project_analysis).and_adds_it_to_the(r.project_analysis_job),
    ):
        r.project_analysis = B.ProjectAnalyses.Models.ProjectAnalysis(
            now=r.project_analysis_job.scheduled_at,
            status="RUNNING",
            job=r.project_analysis_job,
            project=r.project_analysis_job.project,
        )
        r.project_analysis_job.project_analyses.append(r.project_analysis)

    # create project-at-now
    elif match(
        step,
        it()
        .determines_the(r.project_at_now)
        .based_on_the_now_timestamp_of_the(r.project_analysis),
    ):
        r.project_at_now = copy.deepcopy(r.project._actor)
        r.project_at_now._now_ = r.project_analysis.now

    # find default plot list
    elif match(step, it().finds_the(r.default_plot_list).for_the(r.project_at_now)):
        r.default_plot_list = r.project_at_now.plot_lists[0]

    # create plot-analysis
    elif match(
        step,
        it()
        .creates_a(r.plot_analysis)
        .for_the_current(r.plot)
        .and_adds_it_to_the(r.project_analysis),
    ):
        r.plot_analysis = B.PlotAnalyses.Models.PlotAnalysis(
            now=r.project_analysis.now,
            status="RUNNING",
            plot=r.plot,
            project_analysis=r.project_analysis,
        )
        r.project_analysis.plot_analyses.append(r.plot_analysis)

    # create calcium plot-analysis-job
    elif match(step, it().creates_the(r.calcium_plot_analysis_job)):
        r.calcium_plot_analysis_job = S.CalciumPlotAnalysisJob(
            id=r.plot_analysis.id, polygon=r.plot_at_now.polygon
        )
