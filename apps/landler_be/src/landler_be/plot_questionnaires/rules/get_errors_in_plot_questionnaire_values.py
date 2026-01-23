from typing import Dict, Any, List

import pydantic
from plot_questionnaires.schemas import PlotQuestionnaireSchema


def get_errors_in_plot_questionnaire_values(
    values: Dict[str, Any]
) -> List[Dict[str, Any]]:
    try:
        # Validate the values against the schema
        PlotQuestionnaireSchema.validate_model(**values)
        return []  # No errors if validation passes
    except pydantic.ValidationError as e:
        # Convert pydantic validation errors to a list of dicts
        errors = []
        for error in e.errors():
            field = ".".join(str(loc) for loc in error["loc"])
            errors.append({"field": field, "message": error["msg"]})
        return errors
