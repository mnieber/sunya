import glob
import os
from pathlib import Path


def get_scenario_watch_dirs(root_dirname, scenario_spec_patterns):
    """Return the directories to watch (recursively) for the scenario patterns.

    For each pattern, this is the part of the pattern before its first wildcard
    component (e.g. `extra/spec/scenarios` for `extra/spec/scenarios/**/scenario.py`),
    or its nearest existing parent, so that files that are created later are seen.
    """
    watch_dirs = set()
    for pattern in scenario_spec_patterns:
        static_parts = []
        for part in Path(pattern).parts[:-1]:
            if glob.has_magic(part):
                break
            static_parts.append(part)

        watch_dir = Path(root_dirname, *static_parts).resolve()
        while not watch_dir.is_dir() and watch_dir != watch_dir.parent:
            watch_dir = watch_dir.parent
        watch_dirs.add(watch_dir)

    return remove_nested_dirs(watch_dirs)


def remove_nested_dirs(dirs):
    """Drop the dirs that are inside another dir of the set (a recursive watch covers them)."""
    return {
        d
        for d in dirs
        if not any(other != d and d.is_relative_to(other) for other in dirs)
    }


def is_scenario_spec_path(root_dirname, scenario_spec_patterns, path):
    """Return True if path matches one of the scenario patterns."""
    path = os.path.realpath(path)
    for pattern in scenario_spec_patterns:
        matches = glob.glob(os.path.join(root_dirname, pattern), recursive=True)
        if any(os.path.realpath(match) == path for match in matches):
            return True
    return False
