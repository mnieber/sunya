import logging
import os
import yaml
import typing as T
from lcopy.configs.models.config import Config
from lcopy.configs.models.config_node import ConfigNode
from lcopy.configs.models.root_config_node import RootConfigNode
from lcopy.configs.utils.normalize_path import normalize_path

logger = logging.getLogger(__name__)


def parse_config_file(
    config_file: str, config_file_skip_list: T.List[str] = []
) -> Config | None:
    # Normalize the path
    config_file = normalize_path(config_file)

    # Skip if already processed
    if config_file in config_file_skip_list:
        return None

    # Add to skip list
    config_file_skip_list.append(config_file)

    # Check if the config file exists
    if not os.path.isfile(config_file):
        raise FileNotFoundError(f"Config file not found: {config_file}")

    # Read the config file
    with open(config_file, "r") as f:
        config_data = yaml.safe_load(f) or {}

    # Create the Config object
    config = Config()

    # Process includes first
    if "include" in config_data:
        config.include = config_data["include"]

        # Process each included config file
        for include_file in config.include:
            # Get the directory of the current config file
            config_dir = os.path.dirname(config_file)

            # Make the include path relative to the current config file
            include_path = os.path.join(config_dir, include_file)
            include_path = os.path.normpath(include_path)

            # Parse the included config file
            included_config = parse_config_file(include_path, config_file_skip_list)

            # Merge the root config nodes from the included config if not None
            if included_config:
                config.root_config_nodes.extend(included_config.root_config_nodes)

    # Process target section which contains the labels and directory structures
    if "target" in config_data:
        for label, label_data in config_data["target"].items():
            # Create a root config node for this label
            root_node = RootConfigNode(label=label)

            # Process the directory structure for this label
            if isinstance(label_data, dict):
                _process_directory_structure(label_data, root_node)

            # Add the root node to the config
            config.root_config_nodes.append(root_node)

    return config


def _process_directory_structure(
    dir_data: dict, parent_node: T.Union[RootConfigNode, ConfigNode]
) -> None:
    for dirname, contents in dir_data.items():
        # Create a config node for this directory
        if dirname == ".":
            # Special case: '.' means file patterns apply to the current directory
            if isinstance(contents, list):
                # Add file patterns to the parent node
                if isinstance(parent_node, RootConfigNode):
                    # Create a config node for the root level
                    node = ConfigNode(dirname_pattern=".", filename_patterns=contents)
                    parent_node.child_nodes.append(node)
                else:
                    # Add patterns to existing node
                    parent_node.filename_patterns.extend(contents)
            elif isinstance(contents, dict):
                # Process subdirectories
                _process_directory_structure(contents, parent_node)
        else:
            # Regular directory
            if isinstance(contents, list):
                # Directory with file patterns
                node = ConfigNode(dirname_pattern=dirname, filename_patterns=contents)
                parent_node.child_nodes.append(node)
            elif isinstance(contents, dict):
                # Directory with subdirectories
                node = ConfigNode(dirname_pattern=dirname, filename_patterns=[])
                parent_node.child_nodes.append(node)

                # Process subdirectories
                _process_directory_structure(contents, node)
