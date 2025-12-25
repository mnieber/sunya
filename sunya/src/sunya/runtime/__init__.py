from .actions.wipe_spec_files import wipe_spec_files  # noqa
from .actions.write_scenarios import write_scenarios  # noqa
from .utils.parse_args import parse_args  # noqa
from .utils.get_scenario_module_paths import get_scenario_module_paths  # noqa

config = dict(
    prompt_writer_path_tpl="mock.default.{layer}.prompt_writer",
    scenario_path_tpl="mock.blogs.{layer}.scenarios.{scenario_fn}",
    scenario_path_by_name={},
    all_scenario_paths=[
        "backend/ms1_a_user_creates_a_blog.scenario",
        "frontend/ms1_a_user_creates_a_blog.scenario",
    ],
)
