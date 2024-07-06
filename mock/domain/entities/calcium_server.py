from uuid import UUID

from domain.backend.modules.polygons import Polygons
from sunya import Entity, actor_to_str


class CalciumServer(Entity):
    """ """

    url: str


class CalciumPlotAnalysisJob(Entity):
    """ """

    id: UUID
    polygon: Polygons.Models.Polygon


calcium_server = CalciumServer(url="http://calcium:80")


@actor_to_str.method((CalciumServer,))
def calcium_server_to_str(calcium_server):
    return f":calcium-server"


@actor_to_str.method((CalciumPlotAnalysisJob,))
def calcium_plot_analysis_job_to_str(calcium_plot_analysis_job):
    return f"{calcium_plot_analysis_job.id}+:calcium-plot-analysis-job"
