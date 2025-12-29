import glob
import os


def get_module_spec_paths(root_dirname, module_spec_patterns):
    # Expand glob patterns
    module_spec_paths = []
    for pattern in module_spec_patterns:
        # Use glob to find matching files
        matches = glob.glob(os.path.join(root_dirname, pattern), recursive=True)
        module_spec_paths.extend(matches)

    return sorted(module_spec_paths)
