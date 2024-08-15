import glob
import shutil
import os
import argparse
import sys


def get_file_inventory(directory):
    inventory = set()
    for root, _, files in os.walk(directory):
        for file in files:
            inventory.add(os.path.join(root, file))
    return inventory


def get_expanded_dir_list(dir_list):
    result = []
    for dir_entry in dir_list:
        base_dir = dir_entry
        while base_dir:
            if base_dir not in result:
                result.append(base_dir)
            base_dir = os.path.dirname(base_dir)
    return result


def get_files_to_copy(file_map, target_dir, expanded_dir_list):
    files_to_copy = []
    for source_pattern, dest in file_map.items():
        for source in glob.glob(source_pattern):
            if os.path.isfile(source):
                if dest in expanded_dir_list:
                    target = os.path.join(target_dir, dest, os.path.basename(source))
                else:
                    if "." not in os.path.basename(dest):
                        print(
                            "Error: No file extension found in destination file: ",
                            dest,
                            "Did you forget to add an entry in the dir_list?",
                        )
                        sys.exit(1)
                    target = os.path.join(target_dir, dest)
                files_to_copy.append((source, target))
            elif os.path.isdir(source):
                for root, _, files in os.walk(source):
                    for file in files:
                        src_file = os.path.join(root, file)
                        rel_path = os.path.relpath(src_file, source)
                        target = os.path.join(target_dir, dest, rel_path)
                        files_to_copy.append((src_file, target))
    else:
        print(f"Warning: No files found for pattern: {source_pattern}")
    return files_to_copy


def sync_files(file_map, dir_list, target_dir):
    os.makedirs(target_dir, exist_ok=True)
    file_inventory = get_file_inventory(target_dir)
    files_to_copy = get_files_to_copy(
        file_map, target_dir, get_expanded_dir_list(dir_list)
    )

    # Copy files
    for source, target in files_to_copy:
        os.makedirs(os.path.dirname(target), exist_ok=True)
        shutil.copy2(source, target)
        if target in file_inventory:
            file_inventory.remove(target)

    # Remove files that are no longer needed
    for file in file_inventory:
        if os.path.isfile(file):
            os.remove(file)

    # Remove empty directories
    for root, dirs, files in os.walk(target_dir, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)

    return files_to_copy


def parse_args():
    parser = argparse.ArgumentParser(
        description="Synchronize files to a target directory."
    )
    parser.add_argument("target_dir", help="The target directory for synchronization")
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Increase output verbosity"
    )
    args = parser.parse_args()
    return args
