import typing as T

from mock.landler.backend.modules.organizations import Organizations
from mock.landler.backend.modules.polygons import Polygons
from kits.python_app.impl.namespace import Form
from kits.django_app.impl.namespace import Action, ApiView, DjangoModule
from sunya import NowMixin, Entity, FK, RelatedSet

if T.TYPE_CHECKING:
    from mock.landler.backend.modules.plot_questionnaires import PlotQuestionnaires
    from mock.landler.backend.modules.plot_lists import PlotLists


class Plots(DjangoModule):
    class Models:
        class Plot(NowMixin, Entity):
            name: str
            # The (globally unique) sequence_number is used to identify a plot in
            # a user-friendly way. It's similar to a Jira ticket number.
            sequence_number: int
            is_draft: bool = False
            errors: RelatedSet["Plots.Models.PlotError"] = []
            owner: FK[Organizations.Models.Organization]
            polygon: FK[Polygons.Models.Polygon]
            plot_questionnaire: T.Optional[
                FK["PlotQuestionnaires.Models.PlotQuestionnaire"]
            ] = None

        class PlotError(Entity):
            error: str
            plot: FK["Plots.Models.Plot"]
            plot_list: T.Optional[FK["PlotLists.Models.PlotList"]] = None

    class Actions:
        class CreatePlot(Action):
            class Args:
                create_plot_form: Form
                create_polygon_form: Form
                create_plot_questionnaire_form: Form

        class ValidatePlot(Action):
            class Args:
                plot: "Plots.Models.Plot"
                plot_list: T.Optional["PlotLists.Models.PlotList"] = None

    class Api:
        class CreatePlotApiView(ApiView):
            pass
