from dataclassy import dataclass
import typing as T


@dataclass
class Options:
    configs: T.List[str]
    destination: str
    labels: T.List[str]
    conflict: str
    verbose: bool
    purge: bool
    dry_run: bool
    default_ignore: bool
    extra_ignore: T.List[str]

    def get_ignore_patterns(self) -> T.List[str]:
        # Start with standard ignore patterns if default_ignore is True
        patterns = []

        if self.default_ignore:
            # Common version control and temporary files to ignore
            patterns.extend(
                [
                    ".git",
                    ".svn",
                    ".hg",  # Version control
                    "__pycache__",
                    "*.pyc",
                    "*.pyo",
                    ".DS_Store",  # System and cache files
                    "*.swp",
                    "*.swo",  # Vim swap files
                    "*.bak",
                    "*.tmp",
                    "*.temp",  # Backup and temp files
                    "node_modules",
                    "venv",
                    ".env",
                    ".venv",  # Dependencies
                    ".idea",
                    ".vscode",  # IDE files
                ]
            )

        # Add any extra ignore patterns
        if self.extra_ignore:
            patterns.extend(self.extra_ignore)

        return patterns
