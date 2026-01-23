import typing as T

from mock.entities.python_app.namespace import Action, Function, PythonModule, Rule

if T.TYPE_CHECKING:
    from .configs import Configs


class Files(PythonModule):
    class Actions:
        class CopyFiles(Action):
            class Args:
                destination: str
                target_nodes: T.List["Configs.Models.TargetNode"]
                overwrite: str = "skip"
                dry_run: bool = False

                class Returns:
                    copied_files: T.List[str]

        class PurgeFiles(Action):
            class Args:
                destination: str
                files_to_keep: T.List[str]
                dry_run: bool = False

        class CreateConcatenatedOutput(Action):
            class Args:
                concatenated_output_filename: str
                destination: str
                dry_run: bool = False

    class Rules:
        class GetFilteredFiles(Rule):
            class Args:
                files: T.List[str]
                source_dirname: str
                ignore_patterns: T.List[str]
                exclude_patterns: T.List[str]

                class Returns:
                    filtered_files: T.List[str]

    class Utils:
        class NormalizePath(Function):
            class Args:
                rel_path: str
                base_path: str = ""

                class Returns:
                    normalized_path: str

        class ConcatenateDirectory(Function):
            class Args:
                dirname: str
                output_file: str
                exclude_dirs: T.List[str] = None
                exclude_patterns: T.List[str] = None
