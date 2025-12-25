from sunya import FileWriter
from sunya.runtime import (
    wipe_spec_files,
    write_scenarios,
    parse_args,
    get_scenario_module_paths,
)

config = dict(
    prompt_writer_path_tpl="mock.default.{layer}.prompt_writer",
    scenario_path_tpl="mock.landler.{layer}.scenarios.{scenario_fn}",
    scenario_path_by_name={},
    all_scenario_paths=[
        "backend/mrd1_a_user_signs_up.scenario",
        "backend/mrd2_a_user_creates_an_org_and_invites_a_user.scenario",
        "backend/mrd3_a_user_joins_the_demo_org.scenario",
        "backend/mrd4_a_user_creates_a_project.scenario",
        "backend/mrd5_a_user_adds_a_plot_to_a_project.scenario",
        "backend/mrd6_domain_events_are_processed.scenario",
        "backend/mrd7_a_staff_user_schedules_a_project_analysis.scenario",
    ],
)


def run(args):
    scenario_module_paths = get_scenario_module_paths(config, args)

    file_writer = FileWriter("spec/landler")
    wipe_spec_files(file_writer)
    write_scenarios(config, scenario_module_paths, file_writer)


if __name__ == "__main__":
    args = parse_args()
    run(args)
