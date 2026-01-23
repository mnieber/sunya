import typing as T

from mock.entities.python_app.namespace import Action, PythonModule, Rule
from sunya import Entity


class Configs(PythonModule):
    class Models:
        class Config(Entity):
            source_dirname: str
            source_basename: str
            target_nodes: T.List["Configs.Models.TargetNode"] = []
            sources: T.Dict[str, "Configs.Models.SourceConfig"] = {}
            options: T.Optional["Configs.Models.Options"] = None

            @property
            def source_filename(self) -> str:
                return f"{self.source_dirname}/{self.source_basename}"

        class Options(Entity):
            destination: str = ""
            conflict: str = "skip"
            verbose: bool = False
            purge: bool = False
            dry_run: bool = False
            default_ignore: bool = True
            extra_ignore: T.List[str] = []
            labels: T.List[str] = []
            concatenated_output_filename: T.Optional[str] = None

        class SourceConfig(Entity):
            path: str  # Absolute path to the source directory
            alias: str  # Name used to reference this source directory

        class TargetNode(Entity):
            source_dirname: str
            target_basename: str
            filename_patterns: T.List[str]
            child_nodes: T.List["Configs.Models.TargetNode"] = []
            includes: T.List[str] = []  # List of references like "source_alias.label"

    class Actions:
        class ParseConfigFile(Action):
            class Args:
                config_file: str

                class Returns:
                    config: T.Optional["Configs.Models.Config"]

        class ParseTargetNode(Action):
            class Args:
                target_basename: str
                source_dirname: str
                target_node_json: dict
                labels: T.List[str] = None
                ignore_patterns: T.List[str] = None

                class Returns:
                    target_nodes: T.List["Configs.Models.TargetNode"]

        class ParseTargetSection(Action):
            class Args:
                config: "Configs.Models.Config"
                skip_list: T.List[T.Tuple[str, str]]
                ignore_patterns: T.List[str]
                labels: T.List[str]

    class Rules:
        class GetListOfLabels(Rule):
            class Args:
                config_file: str

                class Returns:
                    labels: T.List[str]
