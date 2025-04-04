from sunya import FileWriter
from sunya.runtime import (
    wipe_spec_files,
    write_scenarios,
    parse_args,
    get_scenario_names,
)
import mock.blogs.backend.namespace as B
import mock.blogs.frontend.namespace as F
import kits.django_app.namespace as DefaultB
import kits.react_app.namespace as DefaultF


config = dict(
    prompt_writer_path_tpl="mock.default.{layer}.prompt_writer",
    scenario_path_tpl="mock.blogs.{layer}.scenarios.{scenario_fn}",
    resolve_entity_in_global_namespace=[
        B.resolve_entity_in_global_namespace,
        F.resolve_entity_in_global_namespace,
        DefaultB.resolve_entity_in_global_namespace,
        DefaultF.resolve_entity_in_global_namespace,
    ],
    scenario_path_by_name={},
    all_scenario_names=[
        "backend/ms1_a_user_creates_a_blog",
        "backend/ms2_a_user_creates_a_blog_post",
        "backend/ms3_a_user_edits_and_deletes_a_blog_post",
        "frontend/ms1_a_user_creates_a_blog",
        "frontend/ms2_a_user_creates_a_blog_post",
    ],
)


def run(args):
    scenario_names = get_scenario_names(config, args)

    file_writer = FileWriter("blogs/spec")
    wipe_spec_files(file_writer)
    write_scenarios(config, scenario_names, file_writer)


if __name__ == "__main__":
    args = parse_args()
    run(args)
