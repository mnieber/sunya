from argparse import ArgumentParser

import importlib
from sunya import run_scenario


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--module")
    parser.add_argument("--scenario")
    parser.add_argument("--all", action="store_true")

    return parser.parse_args()


config = dict(
    prompt_writer_path_tpl="default.{layer}.prompt_writer",
    scenario_path_tpl="blogs.{layer}.scenarios.{scenario_fn}",
    scenario_path_by_name={},
    all_module_names=[
        "backend/blogs",
        "frontend/blogs",
    ],
    all_scenario_names=[
        "backend/ms1_a_user_creates_a_blog",
        "frontend/ms1_a_user_creates_a_blog",
    ],
    module_by_name={
        "backend/blogs": None,
        "frontend/blogs": None,
    },
)


def write_scenarios(config, scenario_names, file_writer):
    for idx, scenario_name in enumerate(scenario_names):
        layer, scenario_path = get_scenario_path(config, scenario_name)
        scenario = run_scenario(scenario_path)
        prompt_writer = get_prompt_writer(config, layer)
        scenario_yaml = prompt_writer.get_scenario_description(scenario, idx)
        file_writer.write_scenario(scenario_name, scenario_yaml)


def write_modules(config, module_names, file_writer):
    for module_name in module_names:
        module = config["module_by_name"][module_name]
        layer = module_name.split("/")[0]
        prompt_writer = get_prompt_writer(config, layer)
        module_spec_yaml = prompt_writer.get_module_spec(module)
        file_writer.write_module_spec(module_name, module_spec_yaml)


def wipe_spec_files(file_writer):
    for prefix in ["backend", "frontend"]:
        for pattern in ["modules", "scenarios"]:
            for file in (file_writer.output_dir / prefix / pattern).rglob("*.yaml"):
                file.unlink()


def get_scenario_path(config, scenario_name):
    scenario_path = config["scenario_path_by_name"].get(scenario_name)
    if scenario_path:
        return scenario_path

    parts = scenario_name.split("/")
    assert len(parts) == 2
    layer, scenario_fn = parts
    return layer, config["scenario_path_tpl"].format(
        layer=layer, scenario_fn=scenario_fn
    )


def get_prompt_writer(config, layer):
    prompt_writer_path = config["prompt_writer_path_tpl"].format(layer=layer)
    prompt_writer_pkg = importlib.import_module(prompt_writer_path)
    prompt_writer_class = getattr(prompt_writer_pkg, "PromptWriter")
    return prompt_writer_class()


def get_module_and_scenario_names(config, args):
    use_all_modules = args.all or args.module == "all"
    module_names = (
        config["all_module_names"]
        if use_all_modules
        else [args.module] if args.module else []
    )

    use_all_scenarios = args.all or args.scenario == "all"
    scenario_names = (
        config["all_scenario_names"]
        if use_all_scenarios
        else [args.scenario] if args.scenario else []
    )

    return module_names, scenario_names
