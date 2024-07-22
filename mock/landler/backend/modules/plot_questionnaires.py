import typing as T

from landler.backend.app import Action, Enum, Form, Module
from sunya import Entity, actor_to_str

if T.TYPE_CHECKING:
    from landler.backend.modules.plots import Plots


class PlotQuestionnaires(Module):
    class Models:
        class PlotQuestionnaire(Entity):
            """A Django model that contains a plot questionnaire."""

            plot: T.Optional["Plots.Models.Plot"] = None
            land_type: "PlotQuestionnaires.Enums.LandType"

    class Enums:
        class LandType(Enum):
            CROPLAND = "cropland"
            GRASSLAND = "grassland"

    class Actions:
        class CreatePlotQuestionnaire(Action):
            class Args:
                create_plot_questionnaire_form: Form


create_plot_questionnaire_action = PlotQuestionnaires.Actions.CreatePlotQuestionnaire()


@actor_to_str.method((PlotQuestionnaires.Models.PlotQuestionnaire,))
def plot_questionnaire_to_str(plot_questionnaire):
    return f"{plot_questionnaire.plot.name}+:plot-questionnaire"
