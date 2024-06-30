import typing as T

from mock.backend.modules.organizations import Organizations
from mock.backend.modules.plot_questionnaires import PlotQuestionnaires
from mock.backend.modules.polygons import Polygons
from mock.datatypes import Action, ApiView, Form, Module
from mock.utils.sequence_number_generator import SequenceNumberGenerator
from sunya import Entity, actor_to_str, get_actor_key


class Plots(Module):
    class Models:
        class Plot(Entity):
            """A Django model that contains a plot."""

            name: str
            sequence_number: int
            owner: Organizations.Models.Organization
            polygon: Polygons.Models.Polygon
            plot_questionnaire: T.Optional[
                "PlotQuestionnaires.Models.PlotQuestionnaire"
            ] = None
            is_draft: bool = False
            errors: list[str] = []
            __iteration__: int = 0

    class Actions:
        class CreatePlot(Action):
            class Args:
                create_plot_form: Form

    class Api:
        class CreatePlot(ApiView):
            pass


create_plot_action = Plots.Actions.CreatePlot()
create_plot_api_view = Plots.Api.CreatePlot()


@actor_to_str.method((Plots.Models.Plot,))
def plot_to_str(plot):
    return f"{plot.name}@{plot.__iteration__}+:plot"


@get_actor_key.method((Plots.Models.Plot,))
def get_plot_key(plot):
    return plot.name


plot_sequence_number_generator = SequenceNumberGenerator()
