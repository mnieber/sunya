from argparse import ArgumentParser

from blogs.backend.modules import Blogs as BackendBlogs
from blogs.frontend.modules import Blogs as FrontendBlogs
import importlib
from sunya import FileWriter, run_scenario, get_module_and_scenario_names


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--module")
    parser.add_argument("--scenario")
    parser.add_argument("--all", action="store_true")

    return parser.parse_args()


all_module_names = [
    "backend/blogs",
    "frontend/blogs",
]

all_scenario_names = [
    "backend/ms1_a_user_creates_a_blog",
    "backend/ms2_a_user_creates_a_blog_post",
    "frontend/ms1_a_user_creates_a_blog",
]

module_by_name = {
    "backend/blogs": BackendBlogs,
    "frontend/blogs": FrontendBlogs,
}

scenario_path_by_name = {}


def run(args):
    module_names, scenario_names = get_module_and_scenario_names(
        args, all_module_names, all_scenario_names
    )

    file_writer = FileWriter("blogs/spec")
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
    return f"blogs.backend.scenarios.{parts[-1]}"


def _get_prompt_writer(layer):
    prompt_writer_path = f"blogs.{layer}.prompt_writer"
    prompt_writer_pkg = importlib.import_module(prompt_writer_path)
    prompt_writer_class = getattr(prompt_writer_pkg, "PromptWriter")
    return prompt_writer_class()


if __name__ == "__main__":
    args = parse_args()
    run(args)
