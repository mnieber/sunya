import typing as T

from domain.backend.modules.plots import Plots
from domain.backend.modules.projects import Projects
from domain.datatypes import Action, ApiView, Form, Module
from sunya import Entity, MemField, actor_to_str, extend, get_actor_key


class PlotLists(Module):
    class Models:
        class PlotList(Entity):
            name: str
            plots: T.List[Plots.Models.Plot] = []
            project: Projects.Models.Project

    class Actions:
        class CreatePlot(Action):
            class Args:
                create_plot_form: Form

    class Api:
        class CreatePlot(ApiView):
            pass


create_plot_action = Plots.Actions.CreatePlot()
create_plot_api_view = Plots.Api.CreatePlot()


@actor_to_str.method((PlotLists.Models.PlotList,))
def plot_list_to_str(plot_list):
    return f"{plot_list.name}+:plotList"


@get_actor_key.method((PlotLists.Models.PlotList,))
def get_plot_list_key(plot_list):
    return plot_list.name


@extend(Projects.Models.Project)
class ExtendProject:
    plot_lists = MemField(lambda: list())
