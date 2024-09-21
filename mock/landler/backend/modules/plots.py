import typing as T

from landler.backend.modules.organizations import Organizations
from landler.backend.modules.plot_questionnaires import PlotQuestionnaires
from landler.backend.modules.polygons import Polygons
from default.stack.namespace import Module, Form
from default.backend.namespace import Action, ApiView
from landler.utils.sequence_number_generator import SequenceNumberGenerator
from sunya import get_now_suffix, NowMixin, EntityWithId, actor_to_str, G as g


class Plots(Module):
    class Models:
        class Plot(NowMixin, EntityWithId):
            name: str
            # The (globally unique) sequence_number is used to identify a plot in
            # a user-friendly way. It's similar to a Jira ticket number.
            sequence_number: int
            owner: Organizations.Models.Organization
            polygon: Polygons.Models.Polygon
            plot_questionnaire: T.Optional[
                "PlotQuestionnaires.Models.PlotQuestionnaire"
            ] = None
            is_draft: bool = False
            errors: list[str] = []

    class Actions:
        class CreatePlot(Action):
            class Args:
                create_plot_form: Form

    class Api:
        class CreatePlot(ApiView):
            pass


g.create_plot_action = Plots.Actions.CreatePlot()
g.create_plot_api_view = Plots.Api.CreatePlot()


@actor_to_str.method((Plots.Models.Plot,))
def plot_to_str(plot):
    return f"{plot.name}+:plot{get_now_suffix(plot)}"


plot_sequence_number_generator = SequenceNumberGenerator()
