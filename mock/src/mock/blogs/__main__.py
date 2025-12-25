from sunya import FileWriter
from sunya.runtime import (
    wipe_spec_files,
    write_scenarios,
    parse_args,
    get_scenario_module_paths,
)


config = dict(
    prompt_writer_path_tpl="mock.default.{layer}.prompt_writer",
    scenario_path_tpl="mock.blogs.{layer}.scenarios.{scenario_fn}",
    scenario_path_by_name={},
    all_scenario_paths=[
        "backend/ms1_a_user_creates_a_blog.scenario",
        "backend/ms2_a_user_creates_a_blog_post.scenario",
        "backend/ms3_a_user_edits_and_deletes_a_blog_post.scenario",
        "frontend/ms1_a_user_creates_a_blog.scenario",
        "frontend/ms2_a_user_creates_a_blog_post.scenario",
    ],
)


def run(args):
    scenario_module_paths = get_scenario_module_paths(config, args)

    file_writer = FileWriter("blogs/spec")
    wipe_spec_files(file_writer)
    write_scenarios(config, scenario_module_paths, file_writer)


if __name__ == "__main__":
    args = parse_args()
    run(args)
