from sunya import FileWriter
from sunya.entrypoint import (
    wipe_spec_files,
    write_scenarios,
    parse_args,
    get_scenario_names,
)

config = dict(
    prompt_writer_path_tpl="default.{layer}.prompt_writer",
    scenario_path_tpl="mock.darshana.{layer}.scenarios.{scenario_fn}",
    scenario_path_by_name={},
    all_scenario_names=[
        "frontend/ms1_a_user_creates_a_project",
        "frontend/ms2_a_user_uploads_files_to_a_project",
        "frontend/ms3_a_user_views_a_scenario",
        "backend/ms1_a_user_creates_a_project",
    ],
)


def run(args):
    scenario_names = get_scenario_names(config, args)

    file_writer = FileWriter("darshana/spec")
    wipe_spec_files(file_writer)
    write_scenarios(config, scenario_names, file_writer)


if __name__ == "__main__":
    args = parse_args()
    run(args)
