import tlg_regression_testing.backend.namespace as B
from sunya import FileWriter
from sunya.entrypoint import (
    get_module_and_scenario_names,
    wipe_spec_files,
    write_modules,
    write_scenarios,
    parse_args,
)


config = dict(
    prompt_writer_path_tpl="default.{layer}.prompt_writer",
    scenario_path_tpl="tlg_regression_testing.{layer}.scenarios.{scenario_fn}",
    scenario_path_by_name={},
    all_module_names=[
        "backend/collect",
        "backend/io",
        "backend/selectors",
        "backend/run",
    ],
    all_scenario_names=[
        "backend/ms1_a_user_defines_selectors",
    ],
    module_by_name={
        "backend/collect": B.Collect,
        "backend/selectors": B.Selectors,
        "backend/io": B.IO,
        "backend/run": B.Run,
    },
)


def run(args):
    module_names, scenario_names = get_module_and_scenario_names(config, args)

    file_writer = FileWriter("tlg_regression_testing/spec")
    wipe_spec_files(file_writer)
    write_modules(config, module_names, file_writer)
    write_scenarios(config, scenario_names, file_writer)


if __name__ == "__main__":
    args = parse_args()
    run(args)
