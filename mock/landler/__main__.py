from argparse import ArgumentParser

import importlib
from landler.backend.app import *
from sunya import FileWriter, run_scenario, get_module_and_scenario_names


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--module")
    parser.add_argument("--scenario")
    parser.add_argument("--all", action="store_true")

    return parser.parse_args()


all_module_names = [
    "backend/calculations",
    "backend/facts",
    "backend/organizations",
    "backend/plot_analyses",
    "backend/plot_lists",
    "backend/plot_questionnaires",
    "backend/plots",
    "backend/polygons",
    "backend/project_analyses",
    "backend/project_analysis_jobs",
    "backend/projects",
    "backend/users",
]

all_scenario_names = [
    "s1_a_user_signs_up_and_creates_an_org",
    "s2_a_user_creates_a_project",
    "s3_a_user_adds_a_plot_to_a_project",
    "s4_a_user_schedules_a_project_analysis",
]

module_by_name = {
    "backend/calculations": Calculations,
    "backend/facts": Facts,
    "backend/organizations": Organizations,
    "backend/plot_analyses": PlotAnalyses,
    "backend/plot_lists": PlotLists,
    "backend/plot_questionnaires": PlotQuestionnaires,
    "backend/plots": Plots,
    "backend/polygons": Polygons,
    "backend/project_analyses": ProjectAnalyses,
    "backend/project_analysis_jobs": ProjectAnalysisJobs,
    "backend/projects": Projects,
    "backend/users": Users,
}

scenario_path_by_name = {}


def run(args):
    module_names, scenario_names = get_module_and_scenario_names(
        args, all_module_names, all_scenario_names
    )

    file_writer = FileWriter("landler/spec")
    for module_name in module_names:
        module = module_by_name[module_name]
        layer = module_name.split("/")[0]
        prompt_writer = _get_prompt_writer(layer)
        module_spec_yaml = prompt_writer.get_module_spec(module)
        file_writer.write_module_spec(module_name, module_spec_yaml)

    for scenario_name in scenario_names:
        scenario = run_scenario(
            _get_scenario_path(scenario_path_by_name, scenario_name)
        )
        scenario_yaml = prompt_writer.get_scenario_description(scenario_name, scenario)
        file_writer.write_scenario(scenario_name, scenario_yaml)


def _get_scenario_path(scenario_path_by_name, scenario_name):
    scenario_path = scenario_path_by_name.get(scenario_name)
    if scenario_path:
        return scenario_path

    parts = scenario_name.split("/")
    return f"landler.backend.scenarios.{parts[-1]}"


def _get_prompt_writer(layer):
    prompt_writer_path = f"landler.{layer}.prompt_writer"
    prompt_writer_pkg = importlib.import_module(prompt_writer_path)
    prompt_writer_class = getattr(prompt_writer_pkg, "PromptWriter")
    return prompt_writer_class()


if __name__ == "__main__":
    args = parse_args()
    run(args)
