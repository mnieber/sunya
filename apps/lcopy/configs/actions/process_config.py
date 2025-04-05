import logging
import fnmatch
import os
import glob
import re
from lcopy.configs.models import ConfigNode
from lcopy.filemaps.models import FilemapNode
from lcopy.runtime.models import Options


logger = logging.getLogger(__name__)


def process_config(
    config_node: ConfigNode,
    source_base_dir: str,
    target_base_dir: str,
    file_map_root: FilemapNode,
    options: Options,
) -> None:
    if config_node.dirname_pattern.startswith(
        "("
    ) and config_node.dirname_pattern.endswith(")"):
        _process_regex_pattern(
            config_node, source_base_dir, target_base_dir, file_map_root, options
        )
    else:
        _process_simple_target_directory(
            config_node, source_base_dir, target_base_dir, file_map_root, options
        )


def _process_regex_pattern(
    config_node: ConfigNode,
    source_base_dir: str,
    target_base_dir: str,
    file_map_root: FilemapNode,
    options: Options,
) -> None:
    pattern = config_node.dirname_pattern

    # Extract the variable part from the pattern, which is enclosed in square brackets
    variable_match = re.search(r"\[(.*?)\]", pattern)
    if not variable_match:
        logger.error(
            f"Invalid regex pattern: {pattern}. Must contain a variable part in square brackets."
        )
        return

    variable_part = variable_match.group(1)

    # Create a glob pattern by replacing the variable part with a wildcard
    glob_pattern = re.sub(r"\[(.*?)\]", "*", pattern[1:-1])  # Remove the parentheses
    full_glob_pattern = os.path.join(source_base_dir, glob_pattern)

    # Find all matches for the glob pattern
    matches = glob.glob(full_glob_pattern)

    for match in matches:
        # Extract the part that matched the wildcard
        rel_path = os.path.relpath(match, source_base_dir)
        wildcard_match = re.search(glob_pattern.replace("*", "(.*)"), rel_path)
        if not wildcard_match:
            logger.warning(f"Could not extract variable part from match: {match}")
            continue

        captured_value = wildcard_match.group(1)

        # Create a new target subdirectory using the captured value
        target_subdir = pattern[1:-1].replace(f"[{variable_part}]", captured_value)

        # Create a new config node for this match
        new_config_node = ConfigNode(
            dirname_pattern=match,
            filename_patterns=config_node.filename_patterns,
            child_nodes=config_node.child_nodes,
        )

        # Process this new config node as a simple target directory
        _process_simple_target_directory(
            new_config_node,
            source_base_dir,
            os.path.join(target_base_dir, target_subdir),
            file_map_root,
            options,
        )


def _process_simple_target_directory(
    config_node: ConfigNode,
    source_base_dir: str,
    target_base_dir: str,
    file_map_root: FilemapNode,
    options: Options,
) -> None:
    # Determine the source and target directories
    source_dir = os.path.join(source_base_dir, config_node.dirname_pattern)
    target_dir = target_base_dir

    # Skip if the source directory doesn't exist
    if not os.path.exists(source_dir):
        logger.warning(f"Source directory does not exist: {source_dir}")
        return

    # Create a filemap node for this target directory
    filemap_node = FilemapNode(
        target_path=target_dir,
        source_path=source_dir,
        filenames=[],
        child_nodes=[],
    )

    # Add the filemap node to the file map tree
    file_map_root.child_nodes.append(filemap_node)

    # Get all files in the source directory matching the filename patterns
    all_files = []
    for pattern in config_node.filename_patterns:
        # Check if this is an exclude pattern
        is_exclude = pattern.startswith("!")
        if is_exclude:
            # Skip for now, we'll handle exclusions after collecting all files
            continue

        # Get files matching the include pattern
        full_pattern = os.path.join(source_dir, pattern)
        matching_files = glob.glob(full_pattern)

        # Convert to relative paths
        relative_files = [os.path.relpath(f, source_dir) for f in matching_files]
        all_files.extend(relative_files)

    # Process exclude patterns
    exclude_patterns = [
        p[1:] for p in config_node.filename_patterns if p.startswith("!")
    ]

    # Filter files against ignore patterns and exclude patterns
    filtered_files = []
    for filename in all_files:
        # Check if the file should be ignored based on global ignore patterns
        ignore_patterns = options.get_ignore_patterns() if options else []

        should_ignore = any(
            fnmatch.fnmatch(filename, pattern) for pattern in ignore_patterns
        )
        if should_ignore:
            logger.debug(f"Ignoring file {filename} due to global ignore pattern")
            continue

        # Check if the file should be excluded based on the exclude patterns
        should_exclude = any(
            fnmatch.fnmatch(filename, pattern) for pattern in exclude_patterns
        )
        if should_exclude:
            logger.debug(f"Excluding file {filename} due to exclude pattern")
            continue

        filtered_files.append(filename)

    # Add the filtered files to the filemap node
    filemap_node.filenames = filtered_files

    # Process child nodes recursively
    for child_node in config_node.child_nodes:
        process_config(child_node, source_dir, target_dir, filemap_node, options)
