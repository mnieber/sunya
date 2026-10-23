"""
ConfigContext encapsulates all state related to a single config file.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Set

from sunya.runtime.utils.file_writer import FileWriter


@dataclass
class ConfigContext:
    """
    Encapsulates all state related to processing a single config file.

    Attributes:
        config_path: Absolute path to the config file
        config_dict: Parsed YAML configuration dictionary
        root_dir: Root directory for spec files (relative to config file)
        output_dir: Output directory for rendered documentation
        file_writer: FileWriter instance for this config
        watch_paths: Set of file paths to watch for changes
    """

    component_name: str
    config_path: Path
    config_dict: dict
    root_dir: Path
    output_dir: Path | None
    file_writer: FileWriter | None
    watch_paths: Set[Path]

    def __repr__(self):
        return f"ConfigContext(config_path={self.config_path})"
