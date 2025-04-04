import typing as T

from mock.landler.backend.modules.organizations import Organizations
from mock.landler.backend.modules.plot_questionnaires import PlotQuestionnaires
from mock.landler.backend.modules.polygons import Polygons
from kits.python_app.namespace import Form
from kits.django_app.namespace import Action, ApiView, DjangoModule
from sunya import NowMixin, Entity, FK


class Plots(DjangoModule):
    class Models:
        class Plot(NowMixin, Entity):
            name: str
            # The (globally unique) sequence_number is used to identify a plot in
            # a user-friendly way. It's similar to a Jira ticket number.
            sequence_number: int
            is_draft: bool = False
            errors: list[str] = []
            owner: FK[Organizations.Models.Organization]
            polygon: FK[Polygons.Models.Polygon]
            plot_questionnaire: T.Optional[
                FK["PlotQuestionnaires.Models.PlotQuestionnaire"]
            ] = None

    class Actions:
        class CreatePlot(Action):
            class Args:
                create_plot_form: Form

    class Api:
        class CreatePlotApiView(ApiView):
            pass
