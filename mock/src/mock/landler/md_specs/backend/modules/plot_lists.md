# Module: plot_lists

## PlotLists

```python
class PlotLists(DjangoModule):
    class Models:
        class PlotList(Entity):
            name: str
            plots: RelatedSet[Plots.Models.Plot] = []
            project: FK[Projects.Models.Project]

        class Project2PlotList(Entity):
            plot_list: RelatedSet['PlotLists.Models.PlotList']
            project: FK[Projects.Models.Project]

    class Actions:
        class CreatePlot(Action):
            class Args:
                create_plot_form: Form

    class Api:
        class CreatePlot(ApiView):
            pass
```

