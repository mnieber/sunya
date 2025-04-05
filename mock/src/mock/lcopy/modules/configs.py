import typing as T

from sunya import Entity
from kits.python_app.namespace import PythonModule, Action


class Configs(PythonModule):
    class Models:
        class Config(Entity):
            # List of other lcopy configs to include
            include: T.List[str] = []
            root_config_nodes: T.List["Configs.Models.RootConfigNode"] = []

        class RootConfigNode(Entity):
            label: str
            child_nodes: T.List["Configs.Models.ConfigNode"] = []

        class ConfigNode(Entity):
            # The dirname_pattern indicates a subdirectory of the destination directory.
            #
            # However, there is a special case where the dirname is a regex pattern that
            # is enclosed in brackets and which contains a variable part that is in square
            # brackets such as /some/path/[var]/subdir. In that case, the dirname is
            # interpreted as a relative path to the source directory and the variable part is
            # replaced with a wildcard for glob matching. The match for the wildcard is then
            # used to create the target subdirectory in the destination directory, whereas
            # the full matching path is used as the new source directory for any child nodes.
            dirname_pattern: str
            filename_patterns: T.List[str]
            child_nodes: T.List["Configs.Models.ConfigNode"] = []

    class Actions:
        class ParseConfigFile(Action):
            class Args:
                config_file: str
                # This is the list of config files that have already been processed and
                # should be skipped. Files in this list should have an absolute path.
                # The action should extend this list with the config files that it processes.
                config_file_skip_list: T.List[str] = []

    class Rules:
        pass
