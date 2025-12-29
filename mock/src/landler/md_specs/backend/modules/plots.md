# Module: plots

## Plots

```python
class Plots(DjangoModule):
    class Models:
        class Plot(NowMixin):
            name: str
            sequence_number: int
            is_draft: bool = False
            errors: RelatedSet['Plots.Models.PlotError'] = []
            owner: FK[Organizations.Models.Organization]
            polygon: FK[Polygons.Models.Polygon]
            plot_questionnaire: T.Optional[FK['PlotQuestionnaires.Models.PlotQuestionnaire']] = None

        class PlotError(Entity):
            error: str
            plot: FK['Plots.Models.Plot']
            plot_list: T.Optional[FK['PlotLists.Models.PlotList']] = None

    class Actions:
        class CreatePlot(Action):
            class Args:
                create_plot_form: Form
                create_polygon_form: Form
                create_plot_questionnaire_form: Form

        class ValidatePlot(Action):
            class Args:
                plot: 'Plots.Models.Plot'
                plot_list: T.Optional['PlotLists.Models.PlotList'] = None

    class Api:
        class CreatePlotApiView(ApiView):
            pass
```

