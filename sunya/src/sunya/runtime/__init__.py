from .actions.get_component_markdown import get_component_markdown  # noqa
from .actions.wipe_spec_files import wipe_spec_files  # noqa
from .actions.write_specs import write_specs  # noqa
from .utils.filepath_to_import_path import filepath_to_import_path  # noqa
from .utils.get_module_spec_paths import get_module_spec_paths  # noqa
from .utils.get_scenario_spec_paths import get_scenario_spec_paths  # noqa
from .utils.parse_args import parse_args  # noqa

config = dict(
    scenario_paths=[
        "backend/scenarios/**/scenario.py",
        "frontend/scenarios/**/scenario.py",
    ],
)
