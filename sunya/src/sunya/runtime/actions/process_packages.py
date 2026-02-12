import logging
from sunya.runtime import wipe_spec_files, write_specs

logger = logging.getLogger(__name__)


def process_packages(root_dirname, config, file_writer, verbose=False):
    """
    Process all packages and render their specs.

    Returns a set of directories that contain spec files (for watching).
    """
    watch_paths = set()

    for package, spec_config in config["spec_paths_by_package"].items():
        if verbose:
            logger.debug(f"Processing package: {package}")

        # Determine the output path for this package
        # Default to package name, but allow override via output_dir
        package_output_path = spec_config.get("output_dir", package)

        wipe_spec_files(file_writer, package_output_path)
        more_watch_paths = write_specs(
            root_dirname, package, spec_config, file_writer, package_output_path
        )
        watch_paths.update(more_watch_paths)

    return watch_paths
