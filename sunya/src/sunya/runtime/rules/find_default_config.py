from pathlib import Path


def find_default_config():
    """
    Search for default config file in current directory.

    Looks for (in order):
    - sunya.config.yaml
    - sunya.config.yml
    - .sunya.yaml
    - .sunya.yml
    """
    cwd = Path.cwd()
    candidates = [
        cwd / "sunya.config.yaml",
        cwd / "sunya.config.yml",
        cwd / ".sunya.yaml",
        cwd / ".sunya.yml",
    ]

    for candidate in candidates:
        if candidate.exists():
            return candidate

    return None
