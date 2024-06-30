from sunya import Entity, actor_to_str


class CalciumServer(Entity):
    """ """

    url: str


class CalciumPlotAnalysisJob(Entity):
    """ """

    id: str


calcium_server = CalciumServer(url="http://calcium:80")


@actor_to_str.method((CalciumServer,))
def calcium_server_to_str(calcium_server):
    return f":calcium-server"
