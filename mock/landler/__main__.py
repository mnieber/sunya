from argparse import ArgumentParser

import importlib
import landler.backend.namespace as B
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
    "ms1_a_user_signs_up_and_creates_an_org",
    "ms2_a_user_creates_a_project",
    "ms3_a_user_adds_a_plot_to_a_project",
    "ms4_a_user_schedules_a_project_analysis",
]

module_by_name = {
    "backend/calculations": B.Calculations,
    "backend/facts": B.Facts,
    "backend/organizations": B.Organizations,
    "backend/plot_analyses": B.PlotAnalyses,
    "backend/plot_lists": B.PlotLists,
    "backend/plot_questionnaires": B.PlotQuestionnaires,
    "backend/plots": B.Plots,
    "backend/polygons": B.Polygons,
    "backend/project_analyses": B.ProjectAnalyses,
    "backend/project_analysis_jobs": B.ProjectAnalysisJobs,
    "backend/projects": B.Projects,
    "backend/users": B.Users,
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
        module_spec_yaml = _get_prompt_writer(layer).get_module_spec(module)
        file_writer.write_module_spec(module_name, module_spec_yaml)

    for scenario_name in scenario_names:
        layer, scenario_path = _get_scenario_path(scenario_path_by_name, scenario_name)
        scenario = run_scenario(scenario_path)
        scenario_yaml = _get_prompt_writer(layer).get_scenario_description(
            scenario_name, scenario
        )
        file_writer.write_scenario(scenario_name, scenario_yaml)


def _get_scenario_path(scenario_path_by_name, scenario_name):
    scenario_path = scenario_path_by_name.get(scenario_name)
    if scenario_path:
        return scenario_path

    parts = scenario_name.split("/")
    assert len(parts) == 2
    layer, scenario_fn = parts
    return layer, f"darshana.{layer}.scenarios.{scenario_fn}"


def _get_prompt_writer(layer):
    prompt_writer_path = f"landler.{layer}.prompt_writer"
    prompt_writer_pkg = importlib.import_module(prompt_writer_path)
    prompt_writer_class = getattr(prompt_writer_pkg, "PromptWriter")
    return prompt_writer_class()


if __name__ == "__main__":
    args = parse_args()
    run(args)
