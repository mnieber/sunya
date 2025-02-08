from mock.landler.backend.modules.plots import Plots
from mock.landler.backend.modules.projects import Projects
from mock.python_app.namespace import Form
from mock.django_app.namespace import Action, ApiView


from sunya import Entity, MemField, extend, RelatedSet, FK


class PlotLists(DjangoModule):
    class Models:
        class PlotList(Entity):
            name: str
            plots: RelatedSet[Plots.Models.Plot] = []
            project: FK[Projects.Models.Project]

        class Project2PlotList(Entity):
            plot_list: RelatedSet["PlotLists.Models.PlotList"]
            project: FK[Projects.Models.Project]

    class Actions:
        class CreatePlot(Action):
            class Args:
                create_plot_form: Form

    class Api:
        class CreatePlot(ApiView):
            pass


@extend(Projects.Models.Project)
class ExtendProject:
    plot_lists = MemField(lambda: list())
