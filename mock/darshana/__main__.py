from sunya import FileWriter
from sunya.entrypoint import (
    get_module_and_scenario_names,
    write_modules,
    write_scenarios,
    parse_args,
)


config = dict(
    prompt_writer_path_tpl="default.{layer}.prompt_writer",
    scenario_path_tpl="darshana.{layer}.scenarios.{scenario_fn}",
    scenario_path_by_name={},
    all_module_names=[],
    all_scenario_names=[
        "frontend/ms1_a_user_creates_a_project",
        "frontend/ms1_a_user_views_a_scenario",
    ],
    module_by_name={},
)


def run(args):
    module_names, scenario_names = get_module_and_scenario_names(config, args)

    file_writer = FileWriter("darshana/spec")
    write_modules(config, module_names, file_writer)
    write_scenarios(config, scenario_names, file_writer)


if __name__ == "__main__":
    args = parse_args()
    run(args)
