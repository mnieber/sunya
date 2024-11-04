from dataclassy import dataclass
import typing as T


@dataclass
class FileInfo:
    file_path: str
    function_infos: T.List["FunctionInfo"]
    constants: T.List


@dataclass
class FunctionInfo:
    function_path: str
    caller_paths: T.List[str]
