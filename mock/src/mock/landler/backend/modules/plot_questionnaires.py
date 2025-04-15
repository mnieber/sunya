import typing as T

from kits.python_app.namespace import Form, JSON
from kits.django_app.namespace import Action, DjangoModule
from sunya import Entity


if T.TYPE_CHECKING:
    pass


class PlotQuestionnaires(DjangoModule):
    class Models:
        class PlotQuestionnaire(Entity):
            values: JSON

    class Actions:
        class CreatePlotQuestionnaire(Action):
            class Args:
                create_plot_questionnaire_form: Form

    class Rules:
        class GetErrorsInPlotQuestionnaireValues:
            class Args:
                values: JSON

            class Returns:
                errors: JSON
