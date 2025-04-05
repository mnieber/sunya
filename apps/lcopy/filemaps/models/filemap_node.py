from dataclassy import dataclass
import typing as T


@dataclass
class FilemapNode:
    # Target subdirectory where files will be copied to
    target_path: str

    # Source files are read from this path
    source_path: str

    # List of filenames relative to the source_path
    filenames: T.List[str]

    # Child nodes represent subdirectories
    child_nodes: T.List["FilemapNode"] = []
