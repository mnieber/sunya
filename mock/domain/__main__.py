import importlib
from argparse import ArgumentParser
from pathlib import Path

from domain.app import *
from domain.render.prompt_writer import PromptWriter


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("scenario")

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    scenario_pkg = importlib.import_module(f"domain.scenarios.{args.scenario}")
    run_fn = getattr(scenario_pkg, "run")
    scenario = run_fn()

    prompt_writer = PromptWriter(
        scenario,
        module_order=[
            Calculations,
            Users,
            Organizations,
            Projects,
            Plots,
            ProjectAnalyses,
            PlotAnalyses,
        ]
        + [
            #
            UserAccounts
        ],
        prompts_dir=Path(__file__).parent / "prompts",
    )

    __import__("pudb").set_trace()  # zz
    print(prompt_writer.get_highlevel_description())
    print(prompt_writer.get_modules_description())
    print(prompt_writer.get_scenario_description())

    # print(prompt_writer.get_code_generation_instructions())
