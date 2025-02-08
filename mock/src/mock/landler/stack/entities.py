import typing as T

if T.TYPE_CHECKING:
    from mock.landler.backend.modules.polygons import Polygons

from sunya import Entity


class CalciumServer(Entity):
    url: str  # http://calcium:80


class CalciumPlotAnalysisJob(Entity):
    polygon: "Polygons.Models.Polygon"
