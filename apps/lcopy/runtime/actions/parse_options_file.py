import logging
import os
import yaml
from lcopy.runtime.models.options import Options
from lcopy.configs.utils.normalize_path import normalize_path

logger = logging.getLogger(__name__)


def parse_options_file(options_file: str) -> Options:
    # Normalize the options file path
    options_file = normalize_path(options_file)

    # Check if the options file exists
    if not os.path.isfile(options_file):
        raise FileNotFoundError(f"Options file not found: {options_file}")

    # Read the options file
    with open(options_file, "r") as f:
        options_data = yaml.safe_load(f)

    # Normalize all file paths
    if "configs" in options_data:
        options_data["configs"] = [
            normalize_path(config) for config in options_data.get("configs", [])
        ]

    if "destination" in options_data:
        options_data["destination"] = normalize_path(options_data["destination"])

    # Create the Options object
    options = Options(
        configs=options_data.get("configs", []),
        destination=options_data.get("destination", ""),
        labels=options_data.get("labels", []),
        conflict=options_data.get("conflict", "prompt"),
        verbose=options_data.get("verbose", False),
        purge=options_data.get("purge", False),
        dry_run=options_data.get("dry_run", False),
        default_ignore=options_data.get("default_ignore", True),
        extra_ignore=options_data.get("extra_ignore", []),
    )

    return options
