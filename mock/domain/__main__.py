import importlib
from argparse import ArgumentParser
from pathlib import Path

from domain.app import *
from domain.render.file_writer import FileWriter
from domain.render.prompt_writer import PromptWriter


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--module")
    parser.add_argument("--scenario")
    parser.add_argument("--all", action="store_true")

    return parser.parse_args()


all_modules_names = [
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
    "ms1_a_user_creates_a_blog",
    "s1_a_user_signs_up_and_creates_an_org",
    "s2_a_user_creates_a_project",
    "s3_a_user_adds_a_plot_to_a_project",
    "s4_a_user_schedules_a_project_analysis",
]

if __name__ == "__main__":
    args = parse_args()

    use_all_modules = args.all or args.module == "all"
    module_names = (
        all_modules_names if use_all_modules else [args.module] if args.module else []
    )

    use_all_scenarios = args.all or args.scenario == "all"
    scenario_names = (
        all_scenario_names
        if use_all_scenarios
        else [args.scenario] if args.scenario else []
    )

    file_writer = FileWriter()
    prompt_writer = PromptWriter(prompts_dir=Path(__file__).parent / "prompts")
    for module_name in module_names:
        module_spec_md = prompt_writer.get_module_description(
            module_by_name[module_name]
        )
        file_writer.write_module_spec(module_name, module_spec_md)

    for scenario_name in scenario_names:
        scenario_pkg = importlib.import_module(f"domain.scenarios.{scenario_name}")
        run_fn = getattr(scenario_pkg, "run")
        scenario = run_fn()
        scenario_md = prompt_writer.get_scenario_description(scenario_name, scenario)
        file_writer.write_scenario(scenario_name, scenario_md)
