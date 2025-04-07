import typing as T

from sunya import Entity
from kits.python_app.namespace import PythonModule, Action, JSON, Rule


class Configs(PythonModule):
    class Models:
        class Config(Entity):
            # List of filenames of other lcopy configs to include. These filenames are
            # interpreted relative to the source_dirname.
            include_fns: T.List[str] = []
            # The source dirname is based on the config filename.
            source_dirname: str
            target_nodes: T.List["Configs.Models.TargetNode"] = []

        class TargetNode(Entity):
            # The filename_patterns for this target node are relative to the source dirname.
            # Note that source_dirname is an absolute path.
            source_dirname: str

            # Files for this TargetNode are copied to this subdirectory.
            target_basename: str

            # The filename_patterns are relative to the source_dirname.
            # If a filename pattern matches, then only its base name is used in the
            # destination directory.
            # Filename patterns that start with an exclamation mark
            # are interpreted as patterns to exclude.
            filename_patterns: T.List[str]
            child_nodes: T.List["Configs.Models.TargetNode"] = []

    class Actions:
        # This action creates a Config instance from a config file.
        class ParseConfigFile(Action):
            class Args:
                config_file: str
                # This is the list of config files that have already been processed and
                # should be skipped. Files in this list should have an absolute path.
                # The action should extend this list with the config files that it processes.
                config_file_skip_list: T.List[str] = []
                # If true, then include_fns will be resolved recursively.
                recursive: bool = True

                class Returns:
                    configs: T.List["Configs.Models.Config"]

        # This action creates a TargetNode instance from a target node json in the config file.
        class ParseTargetNode(Action):
            class Args:
                source_dirname: str
                target_node_json: JSON
                # The labels of the target nodes that must be included
                labels: str

                class Returns:
                    target_node: "Configs.Models.TargetNode"

        class CreateConfig(Action):
            pass

        class CreateConfigNode(Action):
            pass

    class Rules:
        class GetListOfLabels(Rule):
            class Args:
                config_file: str

                class Returns:
                    labels: T.List[str]
