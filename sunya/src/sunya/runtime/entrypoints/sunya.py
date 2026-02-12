"""
Sunya CLI entrypoint for rendering markdown documentation from spec files.
"""

import argparse
import sys
import time
from pathlib import Path

import yaml
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from sunya import FileWriter
from sunya.runtime import wipe_spec_files, write_specs
from sunya.runtime.models import ConfigContext
from sunya.runtime.rules.collect_all_configs import collect_all_configs
import logging

logger = logging.getLogger(__name__)


def load_config(config_path):
    """Load configuration from YAML file."""
    if not config_path.exists():
        logger.error(f"Error: Config file not found: {config_path}", file=sys.stderr)
        sys.exit(1)

    with open(config_path, "r") as f:
        try:
            config = yaml.safe_load(f)
        except yaml.YAMLError as e:
            print(f"Error parsing YAML config: {e}", file=sys.stderr)
            sys.exit(1)

    return config


def find_default_config():
    """
    Search for default config file in current directory.

    Looks for (in order):
    - sunya.config.yaml
    - sunya.config.yml
    - .sunya.yaml
    - .sunya.yml
    """
    cwd = Path.cwd()
    candidates = [
        cwd / "sunya.config.yaml",
        cwd / "sunya.config.yml",
        cwd / ".sunya.yaml",
        cwd / ".sunya.yml",
    ]

    for candidate in candidates:
        if candidate.exists():
            return candidate

    return None


def _process_packages(root_dirname, config, file_writer, verbose=False):
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


class SpecFileChangeHandler(FileSystemEventHandler):
    """Handler for spec file changes that triggers re-rendering."""

    def __init__(self, config_contexts, verbose=False):
        """
        Initialize handler for multiple configs.

        Args:
            config_contexts: List of ConfigContext objects to re-render
            verbose: Whether to enable verbose logging
        """
        self.config_contexts = config_contexts
        self.verbose = verbose
        self.last_render_time = 0
        self.debounce_seconds = 1  # Debounce to avoid multiple rapid re-renders

    def should_process_event(self, event):
        """Check if the event should trigger a re-render."""
        if event.is_directory:
            return False

        # Check if the changed file is a Python file
        if not event.src_path.endswith(".py"):
            return False

        # Debounce: avoid processing events that are too close together
        current_time = time.time()
        if current_time - self.last_render_time < self.debounce_seconds:
            return False

        return True

    def on_modified(self, event):
        """Handle file modification events."""
        if not self.should_process_event(event):
            return

        self.render_specs()

    def on_created(self, event):
        """Handle file creation events."""
        if not self.should_process_event(event):
            return

        self.render_specs()

    def render_specs(self):
        """Re-render all specs from all configs."""
        self.last_render_time = time.time()
        logger.info("Change detected, re-rendering all configs...")

        # Track which configs we're re-rendering
        config_paths = [str(ctx.config_path) for ctx in self.config_contexts]
        logger.info(f"Re-rendering {len(config_paths)} config(s):")
        for config_path in config_paths:
            logger.info(f"  - {config_path}")

        success_count = 0
        error_count = 0

        for ctx in self.config_contexts:
            try:
                if "spec_paths_by_package" in ctx.config_dict:
                    _process_packages(
                        ctx.root_dir, ctx.config_dict, ctx.file_writer, self.verbose
                    )
                    success_count += 1
            except Exception as e:
                logger.error(f"Error re-rendering {ctx.config_path}: {e}")
                error_count += 1

        if error_count == 0:
            logger.info(f"✓ Successfully re-rendered {success_count} config(s)")
        else:
            logger.info(
                f"Re-rendering completed with {success_count} success(es) and {error_count} error(s)"
            )


def _create_config_context(config_path: Path, config_dict: dict, verbose: bool) -> ConfigContext:
    """
    Create a ConfigContext from a config file and its dictionary.

    Args:
        config_path: Absolute path to the config file
        config_dict: Parsed YAML configuration
        verbose: Whether to enable verbose logging

    Returns:
        ConfigContext with all fields initialized
    """
    # Determine root directory (where spec files are located)
    # Paths in config are relative to the config file location
    root_dirname = config_path.parent
    if "root_dir" in config_dict:
        root_dirname = (config_path.parent / config_dict["root_dir"]).resolve()
    if root_dirname not in sys.path:
        sys.path.insert(0, str(root_dirname))

    # Determine output directory (required)
    if "output_dir" not in config_dict:
        print(
            f"Error: Config at {config_path} must contain 'output_dir' key",
            file=sys.stderr,
        )
        sys.exit(1)

    output_dir = config_dict["output_dir"]
    if not Path(output_dir).is_absolute():
        output_dir = root_dirname / output_dir
    output_dir = Path(output_dir).resolve()

    # Create file writer
    file_writer = FileWriter(output_dir)

    # Process packages if present
    watch_paths = set()
    if "spec_paths_by_package" in config_dict:
        logger.info(f"Processing config: {config_path}")
        watch_paths = _process_packages(
            root_dirname, config_dict, file_writer, verbose=verbose
        )
        logger.info(f"✓ Documentation rendered to: {output_dir}")

    return ConfigContext(
        config_path=config_path,
        config_dict=config_dict,
        root_dir=root_dirname,
        output_dir=output_dir,
        file_writer=file_writer,
        watch_paths=watch_paths,
    )


def render_command(args):
    """Execute the render command to generate markdown documentation."""
    # Determine config file path
    if args.config:
        config_path = Path(args.config).resolve()
    else:
        config_path = find_default_config()
        if config_path is None:
            logger.error(
                "Error: No config file specified and no default config found.\n"
                "Please provide --config or create a sunya.config.yaml file.",
                file=sys.stderr,
            )
            sys.exit(1)
        logger.info(f"Using config file: {config_path}")

    # Collect all configs (root + referenced)
    all_configs = collect_all_configs(config_path)
    logger.info(f"Found {len(all_configs)} config file(s)")

    # Create ConfigContext for each config
    config_contexts = []
    for cfg_path, cfg_dict in all_configs:
        ctx = _create_config_context(cfg_path, cfg_dict, verbose=args.verbose)
        config_contexts.append(ctx)

    # Count total packages processed
    total_packages = sum(
        len(ctx.config_dict.get("spec_paths_by_package", {}))
        for ctx in config_contexts
    )
    logger.info(f"✓ Processed {len(config_contexts)} configs, rendered {total_packages} packages")

    # If watch mode is enabled, set up file watching
    if args.watch:
        logger.info("Watch mode enabled. Monitoring spec files for changes...")
        logger.info("Press Ctrl+C to stop watching.")

        # Create event handler and observer
        event_handler = SpecFileChangeHandler(
            config_contexts, verbose=args.verbose
        )
        observer = Observer()

        # Watch all paths from all configs
        all_watch_paths = set()
        for ctx in config_contexts:
            all_watch_paths.update(ctx.watch_paths)

        for watch_path in all_watch_paths:
            logger.info(f"Watching file: {watch_path}")
            observer.schedule(event_handler, str(watch_path))

        # Start watching
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            logger.info("\nStopping watch mode...")
            observer.stop()
        observer.join()


def main():
    """Main CLI entrypoint."""
    parser = argparse.ArgumentParser(
        description="Sunya - Generate markdown documentation from spec files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Render command
    render_parser = subparsers.add_parser(
        "render",
        help="Render markdown documentation from spec files",
    )
    render_parser.add_argument(
        "--config",
        "-c",
        help="Path to config file (YAML). If not provided, looks for sunya.config.yaml in current directory.",
    )
    render_parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Enable verbose output",
    )
    render_parser.add_argument(
        "--watch",
        "-w",
        action="store_true",
        help="Watch spec files for changes and automatically re-render",
    )

    args = parser.parse_args()

    if args.command == "render":
        render_command(args)
    elif args.command is None:
        parser.print_help()
        sys.exit(1)
    else:
        logger.error(f"Error: Unknown command '{args.command}'", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
