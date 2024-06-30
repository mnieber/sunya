from mock.backend.modules.plot_lists import PlotLists
from mock.backend.modules.projects import Projects


def get_project_plot_list_by_name(project: Projects.Models.Project, name: str):
    for plot_list in project.plot_lists:
        if plot_list.name == name:
            return plot_list

    plot_list = PlotLists.Models.PlotList(name=name, project=project)
    project.plot_lists.append(plot_list)
    return plot_list
