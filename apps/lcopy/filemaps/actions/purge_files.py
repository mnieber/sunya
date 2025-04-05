import logging
import os
import typing as T
from lcopy.runtime.models import Options

logger = logging.getLogger(__name__)


def purge_files(copied_files: T.List[str], options: Options) -> None:
    destination = options.destination
    logger.info(f"Purging files in destination directory: {destination}")

    # Normalize copied file paths for comparison
    normalized_copied_files = [os.path.normpath(f) for f in copied_files]

    # Walk the destination directory
    for root, dirs, files in os.walk(destination, topdown=False):
        # Process files
        for file in files:
            file_path = os.path.join(root, file)

            # Skip if this file was copied
            if os.path.normpath(file_path) in normalized_copied_files:
                continue

            # Purge the file
            if not options.dry_run:
                logger.info(f"Purging file: {file_path}")
                try:
                    os.remove(file_path)
                except OSError as e:
                    logger.error(f"Failed to purge file {file_path}: {e}")
            else:
                logger.info(f"Would purge file: {file_path}")

        # Process directories (only empty ones since we're using topdown=False)
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)

            # Skip if directory is not empty
            if os.listdir(dir_path):
                continue

            # Purge the directory
            if not options.dry_run:
                logger.info(f"Purging empty directory: {dir_path}")
                try:
                    os.rmdir(dir_path)
                except OSError as e:
                    logger.error(f"Failed to purge directory {dir_path}: {e}")
            else:
                logger.info(f"Would purge empty directory: {dir_path}")
