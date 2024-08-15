import typing as T

from landler.backend.modules.plots import Plots
from landler.backend.modules.projects import Projects
from landler.stack.namespace import Module, Form
from blogs.backend.entities import Action, ApiView


from sunya import Entity, MemField, actor_to_str, extend


class PlotLists(Module):
    class Models:
        class PlotList(Entity):
            name: str
            plots: T.List[Plots.Models.Plot] = []
            project: Projects.Models.Project

        class Project2PlotList(Entity):
            plot_list: "PlotLists.Models.PlotList"
            project: Projects.Models.Project

    class Actions:
        class CreatePlot(Action):
            class Args:
                create_plot_form: Form

    class Api:
        class CreatePlot(ApiView):
            pass


@actor_to_str.method((PlotLists.Models.PlotList,))
def plot_list_to_str(plot_list):
    return f"{plot_list.name}+:plotList"


@extend(Projects.Models.Project)
class ExtendProject:
    plot_lists = MemField(lambda: list())


def get_project_plot_list_by_name(project: Projects.Models.Project, name: str):
    for plot_list in project.plot_lists:
        if plot_list.name == name:
            return plot_list

    plot_list = PlotLists.Models.PlotList(name=name, project=project)
    project.plot_lists.append(plot_list)
    return plot_list
