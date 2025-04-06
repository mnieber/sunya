from kits.python_app.namespace import Action, PythonModule, Rule, Function
import typing as T



if T.TYPE_CHECKING:
    from .configs import Configs


class Files(PythonModule):
    class Actions:
        class CopyFiles(Action):
            class Args:
                # The filemap nodes indicate which files to copy
                target_nodes: T.List["Configs.Models.TargetNode"]
                # The overwrite mode
                overwrite: str

            class Returns:
                # The list of absolute filenames of the copied files
                copied_files: T.List[str]

        class PurgeFiles(Action):
            class Args:
                # Files are purged from this directory
                destination: str
                # The list of absolute filenames of the files that must be kept
                files_to_keep: T.List[str]

    class Rules:
        # Filters the list of files.
        # Files that match the exclude patterns are excluded,
        # where exclude patterns are interpreted relative to
        # the source_direname.
        #
        # Files that match the ignore patterns are also excluded,
        # where ignore patterns are interpreted similar to how
        # gitignore patterns are interpreted.
        class GetFilteredFiles(Rule):
            class Args:
                files: T.List[str]
                source_dirname: str
                ignore_patterns: T.List[str]
                exclude_patterns: T.List[str]

            class Returns:
                filtered_files: T.List[str]

    class Utils:
        # This class returns an absolute normalized path in which environment variables
        # and the user home directory are expanded.
        class NormalizePath(Function):
            class Args:
                base_path: str
                rel_path: str
