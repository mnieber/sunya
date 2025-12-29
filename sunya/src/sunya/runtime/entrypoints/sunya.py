"""
Sunya CLI entrypoint for rendering markdown documentation from spec files.
"""

import argparse
import sys
from pathlib import Path

import yaml

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

    # Process each package
    for package, spec_paths in config["spec_paths_by_package"].items():
        if args.verbose:
            logger.debug(f"Processing package: {package}")

        wipe_spec_files(file_writer, package)
        write_specs(root_dirname, package, spec_paths, file_writer)

    logger.info(f"✓ Documentation rendered to: {output_dir}")


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
