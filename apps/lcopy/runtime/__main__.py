#!/usr/bin/env python3
"""
lcopy - A tool for copying files according to configuration files
"""

import argparse
import logging
import sys

from lcopy.runtime.actions.parse_options_file import parse_options_file
from lcopy.runtime.actions.parse_config_file import parse_config_file
from lcopy.runtime.actions.process_config import process_config
from lcopy.runtime.actions.copy_files import copy_files
from lcopy.runtime.actions.purge_files import purge_files

logger = logging.getLogger(__name__)


def _parse_args():
    parser = argparse.ArgumentParser(
        description="lcopy - A tool for copying files according to configuration files"
    )
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Copy command
    copy_parser = subparsers.add_parser(
        "copy", help="Copy files according to configuration"
    )
    copy_parser.add_argument("--options", required=True, help="Path to options file")

    # Global arguments
    parser.add_argument(
        "-v", "--verbose", action="count", default=0, help="Increase verbosity"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Perform a dry run without actually copying files",
    )

    return parser.parse_args()


def _setup_logging(verbosity):
    log_level = logging.WARNING
    if verbosity >= 2:
        log_level = logging.DEBUG
    elif verbosity >= 1:
        log_level = logging.INFO

    logging.basicConfig(level=log_level, format="%(levelname)s: %(message)s")


def main():
    args = _parse_args()
    _setup_logging(args.verbose)

    if args.command == "copy":
        logger.info(f"Reading options from file: {args.options}")

        # Parse the options file
        options = parse_options_file(args.options)

        # Override dry_run setting if specified in command line
        if args.dry_run:
            options.dry_run = True

        # Create an empty file map tree
        filemap_tree = []

        # Parse each config file and process the root config nodes
        config_file_skip_list = []
        for config_file in options.configs:
            logger.info(f"Processing config file: {config_file}")
            config = parse_config_file(
                config_file, config_file_skip_list=config_file_skip_list
            )

            # Process each root config node
            for root_config_node in config.root_config_nodes:
                if any(label in root_config_node.label for label in options.labels):
                    process_config(root_config_node, filemap_tree, options)

        # Copy the files according to the file map
        copied_files = copy_files(filemap_tree, options)

        # Purge files if required
        if options.purge:
            purge_files(copied_files, options)

        logger.info("Copy operation completed successfully")
    else:
        print("Please specify a command. Use --help for more information.")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
