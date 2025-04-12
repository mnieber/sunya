from sunya import FileWriter
from sunya.runtime import (
    wipe_spec_files,
    write_scenarios,
    parse_args,
    get_scenario_names,
)
import mock.landler.backend.namespace as B
import mock.landler.frontend.namespace as F
import kits.django_app.namespace as DefaultB
import kits.react_app.namespace as DefaultF

config = dict(
    prompt_writer_path_tpl="mock.default.{layer}.prompt_writer",
    scenario_path_tpl="mock.landler.{layer}.scenarios.{scenario_fn}",
    resolve_entity_in_global_namespace=[
        B.resolve_entity_in_global_namespace,
        F.resolve_entity_in_global_namespace,
        DefaultB.resolve_entity_in_global_namespace,
        DefaultF.resolve_entity_in_global_namespace,
    ],
    scenario_path_by_name={},
    all_scenario_names=[
        "backend/mrd1_a_user_signs_up_and_sees_a_checklist",
        "backend/mrd2_a_user_creates_an_org_and_invites_a_user",
        "backend/mrd3_a_user_joins_the_demo_org",
        "backend/mrd4_a_user_creates_a_project",
        "backend/mrd5_a_user_adds_a_plot_to_a_project",
        "backend/mrd6_domain_events_are_processed",
        "backend/mrd7_a_staff_user_schedules_a_project_analysis",
        "frontend/ms2_a_user_interacts_with_the_checklist",
    ],
)


def run(args):
    scenario_names = get_scenario_names(config, args)

    file_writer = FileWriter("spec/landler")
    wipe_spec_files(file_writer)
    write_scenarios(config, scenario_names, file_writer)


if __name__ == "__main__":
    args = parse_args()
    run(args)
