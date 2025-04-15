from dataclassy import dataclass
from typing import Dict, Any

from plot_questionnaires.models import PlotQuestionnaire


@dataclass
class CreatePlotQuestionnaireForm:
    values: Dict[str, Any]


def create_plot_questionnaire(
    create_plot_questionnaire_form: CreatePlotQuestionnaireForm,
) -> PlotQuestionnaire:
    errors = get_errors_in_plot_questionnaire_values(
        create_plot_questionnaire_form.values
    )
    if errors:
        raise InvalidPlotQuestionnaireFormatError(errors)

    crc = None  # TODO

    # Create the plot_questionnaire
    plot_questionnaire = PlotQuestionnaire(
        values=create_plot_questionnaire_form.values, crc=crc
    )
    plot_questionnaire.save()

    return plot_questionnaire


class InvalidPlotQuestionnaireFormatError(Exception):
    pass
