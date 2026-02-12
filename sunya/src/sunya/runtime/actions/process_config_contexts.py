import logging
from sunya.runtime import wipe_spec_files, write_specs
from sunya.scenarios.actions.create_component import create_component

logger = logging.getLogger(__name__)


def process_config_contexts(config_contexts, verbose=False):
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
            if verbose:
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

    return count
