from sunya import FileWriter
from sunya.entrypoint import (
    wipe_spec_files,
    write_scenarios,
    parse_args,
    get_scenario_module_paths,
)

config = dict(
    prompt_writer_path_tpl="default.{layer}.prompt_writer",
    scenario_path_tpl="mock.darshana.{layer}.scenarios.{scenario_fn}",
    scenario_path_by_name={},
    all_scenario_paths=[
        "frontend/ms1_a_user_creates_a_project.scenario",
        "frontend/ms2_a_user_uploads_files_to_a_project.scenario",
        "frontend/ms3_a_user_views_a_scenario.scenario",
        "backend/ms1_a_user_creates_a_project.scenario",
    ],
)


def run(args):
    scenario_module_paths = get_scenario_module_paths(config, args)

    file_writer = FileWriter("darshana/spec")
    wipe_spec_files(file_writer)
    write_scenarios(config, scenario_module_paths, file_writer)


if __name__ == "__main__":
    args = parse_args()
    run(args)
