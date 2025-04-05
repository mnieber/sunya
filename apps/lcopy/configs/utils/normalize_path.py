import os


def normalize_path(path: str) -> str:
    # Expand environment variables (e.g., $HOME)
    expanded_path = os.path.expandvars(path)

    # Expand user directory (the ~ character)
    expanded_path = os.path.expanduser(expanded_path)

    # Convert to absolute path
    absolute_path = os.path.abspath(expanded_path)

    # Normalize the path (resolve '..' and '.')
    normalized_path = os.path.normpath(absolute_path)

    return normalized_path
