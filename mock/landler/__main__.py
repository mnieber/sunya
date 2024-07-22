from argparse import ArgumentParser

from landler.backend.app import *
from sunya import FileWriter, run_scenario, get_module_and_scenario_names
from landler.backend.prompt_writer import PromptWriter


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--module")
    parser.add_argument("--scenario")
    parser.add_argument("--all", action="store_true")

    return parser.parse_args()


all_module_names = [
    "calculations",
    "users",
    "organizations",
    "projects",
    "plots",
    "project_analyses",
    "plot_analyses",
]

module_by_name = dict(
    calculations=Calculations,
    users=Users,
    organizations=Organizations,
    projects=Projects,
    plots=Plots,
    project_analyses=ProjectAnalyses,
    plot_analyses=PlotAnalyses,
)

all_scenario_names = [
    "s1_a_user_signs_up_and_creates_an_org",
    "s2_a_user_creates_a_project",
    "s3_a_user_adds_a_plot_to_a_project",
    "s4_a_user_schedules_a_project_analysis",
]

if __name__ == "__main__":
    args = parse_args()

    module_names, scenario_names = get_module_and_scenario_names(
        args, all_module_names, all_scenario_names
    )

    file_writer = FileWriter("landler/.output")
    prompt_writer = PromptWriter(templates_dir="landler/templates")
    for module_name in module_names:
        module_spec_md = prompt_writer.get_module_description(
            module_by_name[module_name]
        )
        file_writer.write_module_spec(module_name, module_spec_md)

    for scenario_name in scenario_names:
        scenario = run_scenario(f"landler.scenarios.{scenario_name}")
        scenario_md = prompt_writer.get_scenario_description(scenario_name, scenario)
        file_writer.write_scenario(scenario_name, scenario_md)
