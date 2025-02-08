import typing as T

from mock.python_app.namespace import Enum, Form
from mock.django_app.namespace import Action, DjangoModule
from sunya import Entity, FK


if T.TYPE_CHECKING:
    from mock.landler.backend.modules.plots import Plots


class PlotQuestionnaires(DjangoModule):
    class Models:
        class PlotQuestionnaire(Entity):
            land_type: "PlotQuestionnaires.Enums.LandType"
            plot: FK["Plots.Models.Plot"]

    class Enums:
        class LandType(Enum):
            CROPLAND = "cropland"
            GRASSLAND = "grassland"

    class Actions:
        class CreatePlotQuestionnaire(Action):
            class Args:
                create_plot_questionnaire_form: Form
