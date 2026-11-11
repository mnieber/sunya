"""
Sunya CLI entrypoint for rendering markdown documentation from spec files.
"""

import argparse
import logging
import sys
from pathlib import Path

from sunya.config.actions.create_config_context import create_config_context
from sunya.config.rules.collect_all_configs import collect_all_configs
from sunya.config.rules.find_default_config import find_default_config
from sunya.render.actions.render_specs import render_specs
from sunya.render.actions.watch_and_render import watch_and_render
from sunya.utils.get_logger import get_logger

logger = get_logger()
logger.setLevel(logging.INFO)


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
        ctx = create_config_context(cfg_path, cfg_dict)
        config_contexts.append(ctx)

    # Render specs for all configs
    count = render_specs(
        config_contexts,
        reset_store=True,
        create_simple_output_dir=args.create_simple_output_dir,
    )

    # Count total packages processed
    logger.info(f"✓ Processed {count} configs")

    if args.watch:
        watch_and_render(
            config_contexts,
            create_simple_output_dir=args.create_simple_output_dir,
            poll_interval=args.poll_interval,
        )


def serve_command(args):
    """Execute the serve command to start a file server for the simple scenarios directory."""
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

    # Collect all configs and create root config context
    all_configs = collect_all_configs(config_path)
    root_config_path, root_config_dict = all_configs[0]
    root_config_context = create_config_context(root_config_path, root_config_dict)

    if not root_config_context.output_dir:
        logger.error(
            "Error: No output_dir specified in config file.",
            file=sys.stderr,
        )
        sys.exit(1)

    # Check if store directory exists
    store_dir = root_config_context.output_dir / "store"
    if not store_dir.exists():
        logger.error(
            f"Error: Store directory does not exist: {store_dir}\n"
            "Please run 'sunya render --create-simple-output-dir' first.",
            file=sys.stderr,
        )
        sys.exit(1)

    # Start HTTP server
    import http.server
    import os
    import socketserver

    port = args.port
    os.chdir(store_dir)

    handler = http.server.SimpleHTTPRequestHandler

    # Allow socket reuse to prevent "Address already in use" errors
    socketserver.TCPServer.allow_reuse_address = True

    with socketserver.TCPServer(("", port), handler) as httpd:
        logger.info(f"Serving scenarios at http://localhost:{port}")
        logger.info(f"Serving from directory: {store_dir}")
        logger.info("Press Ctrl+C to stop the server.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            logger.info("\nStopping server...")
            httpd.shutdown()


def main():
    """Main CLI entrypoint."""
    parser, args = _parse_args()

    if args.verbose:
        logger.setLevel(logging.DEBUG)
        logger.debug("Verbose mode enabled")

    if args.command == "render":
        render_command(args)
    elif args.command == "serve":
        serve_command(args)
    elif args.command is None:
        parser.print_help()
        sys.exit(1)
    else:
        logger.error(f"Error: Unknown command '{args.command}'", file=sys.stderr)
        sys.exit(1)


def _parse_args():
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
    render_parser.add_argument(
        "--poll-interval",
        type=float,
        default=None,
        help="Poll interval in seconds for file watching (recommended for Docker, e.g., 5). If not set, uses native file system events.",
    )
    render_parser.add_argument(
        "--create-simple-output-dir",
        action="store_true",
        help="Create a simple 'store' directory structure with scenarios",
    )

    # Serve command
    serve_parser = subparsers.add_parser(
        "serve",
        help="Serve the simple scenarios directory via HTTP",
    )
    serve_parser.add_argument(
        "--config",
        "-c",
        help="Path to config file (YAML). If not provided, looks for sunya.config.yaml in current directory.",
    )
    serve_parser.add_argument(
        "--port",
        "-p",
        type=int,
        default=8000,
        help="Port to run the HTTP server on (default: 8000)",
    )

    args = parser.parse_args()
    return parser, args


if __name__ == "__main__":
    main()
