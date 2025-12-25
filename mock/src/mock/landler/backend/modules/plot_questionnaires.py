import typing as T

from kits.python_app.impl.namespace import Form, JSON, Schema
from kits.django_app.impl.namespace import Action, DjangoModule
from sunya import Entity


if T.TYPE_CHECKING:
    pass


class PlotQuestionnaires(DjangoModule):
    class Models:
        class PlotQuestionnaire(Entity):
            values: JSON
            schema_version: str

    class Actions:
        class CreatePlotQuestionnaire(Action):
            class Args:
                create_plot_questionnaire_form: Form

    class Schemas:
        class PlotQuestionnaireSchema(Schema):
            pass

    class Rules:
        class GetErrorsInPlotQuestionnaireValues:
            class Args:
                values: JSON

            class Returns:
                errors: JSON
