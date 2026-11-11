import glob
import os


def get_scenario_spec_paths(root_dirname, scenario_spec_patterns):
    # Expand glob patterns
    scenario_spec_paths = []
    for pattern in scenario_spec_patterns:
        # Use glob to find matching files
        matches = glob.glob(os.path.join(root_dirname, pattern), recursive=True)
        scenario_spec_paths.extend(
            os.path.relpath(match, root_dirname) for match in matches
        )

    return sorted(scenario_spec_paths)
