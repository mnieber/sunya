from sunya.runtime import wipe_spec_files, write_specs
from sunya.runtime.utils.get_logger import get_logger
from sunya.scenarios.actions.create_component import create_component
from sunya.runtime.actions.create_simple_scenarios_dir import (
    create_simple_scenarios_dir,
)
from sunya.scenarios.models.store import get_store

logger = get_logger()


def process_config_contexts(
    config_contexts, *, reset_store: bool, create_simple_output_dir: bool
) -> int:
    if reset_store:
        get_store().reset()

    count = 0

    for config_context in config_contexts:
        if "spec_paths_by_package" not in config_context.config_dict:
            continue

        # Create a component in the spec store
        create_component(config_context.component_name)

        config_context.watch_paths = set()
        for package, spec_config in config_context.config_dict[
            "spec_paths_by_package"
        ].items():
            logger.debug(f"Processing package: {package}")

            # Determine the output path for this package
            # Default to package name, but allow override via output_dir
            package_output_path = spec_config.get("output_dir", package)

            wipe_spec_files(config_context.file_writer, package_output_path)
            more_watch_paths = write_specs(
                config_context.root_dir,
                package,
                spec_config,
                config_context.file_writer,
                package_output_path,
            )
            config_context.watch_paths.update(more_watch_paths)
            count += 1

            # Create simple scenarios directory if requested
            if create_simple_output_dir:
                create_simple_scenarios_dir(config_contexts[0])

    return count
