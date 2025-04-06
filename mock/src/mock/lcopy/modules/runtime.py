import typing as T

from sunya import Entity
from kits.python_app.entities import PythonModule, Rule


class Runtime(PythonModule):
    class Models:
        class Options(Entity):
            config_fns: T.List[str]
            destination: str
            labels: T.List[str]
            conflict: str
            verbose: bool
            purge: bool
            dry_run: bool
            default_ignore: bool
            extra_ignore: T.List[str]

    class Actions:
        pass

    class Rules:
        # Returns the list of ignore patterns based on default_ignore
        # and extra_ignore.
        class GetIgnorePatterns(Rule):
            class Args:
                default_ignore: bool
                extra_ignore: T.List[str]

            class Returns:
                ignore_patterns: T.List[str]
