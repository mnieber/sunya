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
    watch_dirs = set()

    for package, spec_paths in config["spec_paths_by_package"].items():
        if verbose:
            logger.debug(f"Processing package: {package}")

        wipe_spec_files(file_writer, package)
        write_specs(root_dirname, package, spec_paths, file_writer)

        # Collect directories containing spec files
        for spec_path in spec_paths:
            # Convert spec path to absolute path
            if not Path(spec_path).is_absolute():
                spec_path = root_dirname / spec_path
            else:
                spec_path = Path(spec_path)

            # Add the directory containing the spec file
            watch_dirs.add(spec_path.parent)

    return watch_dirs


class SpecFileChangeHandler(FileSystemEventHandler):
    """Handler for spec file changes that triggers re-rendering."""

    def __init__(self, root_dirname, config, file_writer, verbose=False):
        self.root_dirname = root_dirname
        self.config = config
        self.file_writer = file_writer
        self.verbose = verbose
        self.last_render_time = 0
        self.debounce_seconds = 1  # Debounce to avoid multiple rapid re-renders

    def should_process_event(self, event):
        """Check if the event should trigger a re-render."""
        if event.is_directory:
            return False

        # Check if the changed file is a Python file
        if not event.src_path.endswith('.py'):
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
        """Re-render all specs."""
        self.last_render_time = time.time()
        logger.info("Change detected, re-rendering specs...")

        try:
            _process_packages(self.root_dirname, self.config, self.file_writer, self.verbose)
            logger.info("✓ Documentation re-rendered successfully")
        except Exception as e:
            logger.error(f"Error during re-rendering: {e}")


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

    # Load configuration
    config = load_config(config_path)

    # Validate config structure
    if "spec_paths_by_package" not in config:
        logger.error(
            "Error: Config must contain 'spec_paths_by_package' key",
            file=sys.stderr,
        )
        sys.exit(1)

    # Determine root directory (where spec files are located)
    # Paths in config are relative to the config file location
    root_dirname = config_path.parent
    if "root_dir" in config:
        root_dirname = (config_path.parent / config["root_dir"]).resolve()
    if root_dirname not in sys.path:
        sys.path.insert(0, str(root_dirname))

    # Determine output directory
    output_dir = config.get("output_dir", "md_specs")
    if not Path(output_dir).is_absolute():
        output_dir = root_dirname / output_dir

    # Create file writer
    file_writer = FileWriter(output_dir)

    # Process each package and get directories to watch
    watch_dirs = _process_packages(root_dirname, config, file_writer, verbose=args.verbose)

    logger.info(f"✓ Documentation rendered to: {output_dir}")

    # If watch mode is enabled, set up file watching
    if args.watch:
        logger.info("Watch mode enabled. Monitoring spec files for changes...")
        logger.info("Press Ctrl+C to stop watching.")

        # Create event handler and observer
        event_handler = SpecFileChangeHandler(
            root_dirname, config, file_writer, verbose=args.verbose
        )
        observer = Observer()

        # Watch each directory
        for watch_dir in watch_dirs:
            logger.info(f"Watching directory: {watch_dir}")
            observer.schedule(event_handler, str(watch_dir), recursive=True)

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
