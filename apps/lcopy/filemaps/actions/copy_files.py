import logging
import os
import shutil
import typing as T
from lcopy.filemaps.models import FilemapNode
from lcopy.runtime.models import Options

logger = logging.getLogger(__name__)


def copy_files(filemap_tree: T.List[FilemapNode], options: Options) -> T.List[str]:
    # List to track all copied destination files
    copied_files = []

    # Process each node in the file map tree
    for node in filemap_tree:
        _copy_files_for_node(node, options, copied_files)

    return copied_files


def _copy_files_for_node(
    node: FilemapNode, options: Options, copied_files: T.List[str]
) -> None:
    # Create the target directory if it doesn't exist
    if not os.path.exists(node.target_path) and not options.dry_run:
        logger.debug(f"Creating directory: {node.target_path}")
        os.makedirs(node.target_path, exist_ok=True)

    # Copy each file
    for filename in node.filenames:
        source_file = os.path.join(node.source_path, filename)
        target_file = os.path.join(node.target_path, filename)

        # Create subdirectories for the target file if needed
        target_dir = os.path.dirname(target_file)
        if not os.path.exists(target_dir) and not options.dry_run:
            logger.debug(f"Creating directory: {target_dir}")
            os.makedirs(target_dir, exist_ok=True)

        # Check if target file exists
        if os.path.exists(target_file):
            should_copy = _handle_conflict(source_file, target_file, options)
            if not should_copy:
                logger.info(f"Skipping file: {target_file}")
                continue

        # Copy the file
        if not options.dry_run:
            logger.info(f"Copying file: {source_file} -> {target_file}")
            shutil.copy2(source_file, target_file)
        else:
            logger.info(f"Would copy file: {source_file} -> {target_file}")

        # Add to the list of copied files
        copied_files.append(target_file)

    # Process child nodes recursively
    for child_node in node.child_nodes:
        _copy_files_for_node(child_node, options, copied_files)


def _handle_conflict(source_file: str, target_file: str, options: Options) -> bool:
    conflict_strategy = options.conflict.lower()

    if conflict_strategy == "overwrite":
        logger.debug(f"Overwriting existing file: {target_file}")
        return True

    elif conflict_strategy == "skip":
        logger.debug(f"Skipping existing file: {target_file}")
        return False

    elif conflict_strategy == "prompt":
        if options.dry_run:
            logger.info(f"Would prompt for conflict resolution: {target_file}")
            return True

        # Compare modification times
        source_mtime = os.path.getmtime(source_file)
        target_mtime = os.path.getmtime(target_file)

        if source_mtime > target_mtime:
            msg = f"Source file is newer: {source_file}"
        elif source_mtime < target_mtime:
            msg = f"Target file is newer: {target_file}"
        else:
            msg = f"Source and target files have the same modification time"

        # Prompt the user
        while True:
            answer = input(
                f"File exists: {target_file}\n{msg}\nOverwrite? (y/n): "
            ).lower()
            if answer in ("y", "yes"):
                return True
            elif answer in ("n", "no"):
                return False

    # Default to skip if strategy is unknown
    logger.warning(
        f"Unknown conflict strategy: {conflict_strategy}, defaulting to skip"
    )
    return False
