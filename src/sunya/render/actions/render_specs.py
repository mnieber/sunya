from sunya.render.actions.create_simple_scenarios_dir import (
    create_simple_scenarios_dir,
)
from sunya.render.actions.wipe_spec_files import wipe_spec_files
from sunya.render.actions.write_specs import write_specs
from sunya.scenarios.actions.create_component import create_component
from sunya.scenarios.models.store import get_store
from sunya.utils.get_logger import get_logger

logger = get_logger()


def render_specs(
    config_contexts, *, reset_store: bool, create_simple_output_dir: bool
) -> int:
    if reset_store:
        get_store().reset()

    count = 0

    for config_context in config_contexts:
        package_config_by_name = config_context.config_dict.get(
            "package_config_by_name"
        )
        if not package_config_by_name:
            continue

        # Create a component in the spec store
        create_component(config_context.component_name)

        config_context.watch_paths = set()
        for package_name, package_config in package_config_by_name.items():
            logger.debug(f"Processing package: {package_name}")

            # Determine the output path for this package
            # Default to package name, but allow override via output_dir
            package_output_path = package_config.get("output_dir", package_name)

            wipe_spec_files(config_context.file_writer, package_output_path)
            more_watch_paths = write_specs(
                config_context.root_dir,
                package_name,
                package_config,
                config_context.file_writer,
                package_output_path,
            )
            config_context.watch_paths.update(more_watch_paths)
            count += 1

            # Create simple scenarios directory if requested
            if create_simple_output_dir:
                create_simple_scenarios_dir(config_contexts[0])

    return count
