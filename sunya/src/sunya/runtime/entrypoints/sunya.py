"""
Sunya CLI entrypoint for rendering markdown documentation from spec files.
"""

import argparse
import sys
import time
from pathlib import Path

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from sunya.runtime.actions.create_config_context import create_config_context
from sunya.runtime.actions.process_packages import process_packages
from sunya.runtime.rules.collect_all_configs import collect_all_configs
import logging

logger = logging.getLogger(__name__)


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
                    process_packages(
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


def render_command(args):
    """Execute the render command to generate markdown documentation."""
    # Determine config file path
    if args.config:
        config_path = Path(args.config).resolve()
    else:
        config_path = _find_default_config()
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
        ctx = create_config_context(cfg_path, cfg_dict, verbose=args.verbose)
        config_contexts.append(ctx)

    # Count total packages processed
    total_packages = sum(
        len(ctx.config_dict.get("spec_paths_by_package", {})) for ctx in config_contexts
    )
    logger.info(
        f"✓ Processed {len(config_contexts)} configs, rendered {total_packages} packages"
    )

    # If watch mode is enabled, set up file watching
    if args.watch:
        logger.info("Watch mode enabled. Monitoring spec files for changes...")
        logger.info("Press Ctrl+C to stop watching.")

        # Create event handler and observer
        event_handler = SpecFileChangeHandler(config_contexts, verbose=args.verbose)
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


def _find_default_config():
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


if __name__ == "__main__":
    main()
