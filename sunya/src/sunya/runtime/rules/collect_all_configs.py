"""
Recursively collect all config files referenced in a root config.
"""

import os
import sys
from pathlib import Path
from typing import List, Tuple, Set

import yaml


def collect_all_configs(root_config_path: Path) -> List[Tuple[Path, dict]]:
    """
    Recursively collect all config files starting from the root config.

    Resolves paths with support for:
    - Relative paths (relative to parent config)
    - Absolute paths
    - Home directory expansion (~)
    - Environment variable expansion

    Args:
        root_config_path: Path to the root configuration file

    Returns:
        List of (config_path, config_dict) tuples for all configs found

    Raises:
        FileNotFoundError: If a referenced config file doesn't exist
        ValueError: If a circular reference is detected
        yaml.YAMLError: If a config file has invalid YAML syntax
    """
    visited: Set[Path] = set()
    result: List[Tuple[Path, dict]] = []

    def _collect_recursive(config_path: Path, parent_path: Path = None):
        # Resolve the config path
        resolved_path = _resolve_config_path(config_path, parent_path)

        # Check if file exists
        if not resolved_path.exists():
            print(f"Error: Config file not found: {resolved_path}", file=sys.stderr)
            sys.exit(1)

        # Detect circular references
        if resolved_path in visited:
            print(
                f"Error: Circular reference detected in config files: {resolved_path}",
                file=sys.stderr,
            )
            sys.exit(1)

        visited.add(resolved_path)

        # Load the config
        with open(resolved_path, "r") as f:
            try:
                config_dict = yaml.safe_load(f)
            except yaml.YAMLError as e:
                print(
                    f"Error parsing YAML config at {resolved_path}: {e}",
                    file=sys.stderr,
                )
                sys.exit(1)

        # Add this config to results
        result.append((resolved_path, config_dict))

        # Recursively process referenced configs
        if "configs" in config_dict and config_dict["configs"]:
            for referenced_config_path in config_dict["configs"]:
                _collect_recursive(
                    Path(referenced_config_path), parent_path=resolved_path.parent
                )

    _collect_recursive(root_config_path)
    return result


def _resolve_config_path(config_path: Path, parent_dir: Path = None) -> Path:
    """
    Resolve a config path with support for relative, absolute, ~, and env vars.

    Args:
        config_path: The path to resolve
        parent_dir: Parent directory for relative path resolution

    Returns:
        Resolved absolute Path
    """
    path_str = str(config_path)

    # Expand environment variables
    path_str = os.path.expandvars(path_str)

    # Expand home directory
    path_str = os.path.expanduser(path_str)

    resolved = Path(path_str)

    # If not absolute and parent_dir provided, resolve relative to parent
    if not resolved.is_absolute() and parent_dir is not None:
        resolved = (parent_dir / resolved).resolve()
    else:
        resolved = resolved.resolve()

    return resolved
