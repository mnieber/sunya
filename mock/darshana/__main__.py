from sunya import FileWriter
from sunya.entrypoint import (
    get_module_and_scenario_names,
    write_modules,
    write_scenarios,
    parse_args,
)
import darshana.frontend.namespace as F
import darshana.backend.namespace as B

config = dict(
    prompt_writer_path_tpl="default.{layer}.prompt_writer",
    scenario_path_tpl="darshana.{layer}.scenarios.{scenario_fn}",
    scenario_path_by_name={},
    all_module_names=[
        "frontend/actors",
        "frontend/projects",
        "frontend/scenarios",
        "frontend/steps",
        "frontend/users",
        "backend/actors",
        "backend/projects",
        "backend/scenarios",
        "backend/steps",
    ],
    all_scenario_names=[
        "frontend/ms1_a_user_creates_a_project",
        "frontend/ms2_a_user_uploads_files_to_a_project",
        "frontend/ms3_a_user_views_a_scenario",
        "backend/ms1_a_user_creates_a_project",
    ],
    module_by_name={
        "frontend/actors": F.Actors,
        "frontend/projects": F.Projects,
        "frontend/scenarios": F.Scenarios,
        "frontend/steps": F.Steps,
        "frontend/users": F.Users,
        "backend/actors": B.Actors,
        "backend/projects": B.Projects,
        "backend/scenarios": B.Scenarios,
        "backend/steps": B.Steps,
    },
)


def run(args):
    module_names, scenario_names = get_module_and_scenario_names(config, args)

    file_writer = FileWriter("darshana/spec")
    write_modules(config, module_names, file_writer)
    write_scenarios(config, scenario_names, file_writer)


if __name__ == "__main__":
    args = parse_args()
    run(args)
