# Module: plot_questionnaires

## PlotQuestionnaires

```python
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
```

