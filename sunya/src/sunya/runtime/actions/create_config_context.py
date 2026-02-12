import sys
from pathlib import Path


from sunya import FileWriter
from sunya.runtime.models import ConfigContext
import logging

logger = logging.getLogger(__name__)


def create_config_context(config_path: Path, config_dict: dict) -> ConfigContext:
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

    # Determine output directory (required if there is a spec_paths_by_package key)
    if "spec_paths_by_package" in config_dict:
        if "output_dir" not in config_dict:
            raise ValueError(
                f"Error: Config at {config_path} must contain 'output_dir' key",
            )
        if not config_dict.get("component_name"):
            raise ValueError(
                f"Error: Config at {config_path} must contain 'component_name' key",
            )

    # Create file_writer
    file_writer = None
    output_dir = None
    if output_dir := config_dict.get("output_dir"):
        if not Path(output_dir).is_absolute():
            output_dir = root_dirname / output_dir
        output_dir = Path(output_dir).resolve()

        # Create file writer
        file_writer = FileWriter(output_dir)

    return ConfigContext(
        component_name=config_dict.get("component_name", "root"),
        config_path=config_path,
        config_dict=config_dict,
        root_dir=root_dirname,
        output_dir=output_dir,
        file_writer=file_writer,
        watch_paths=set(),
    )
