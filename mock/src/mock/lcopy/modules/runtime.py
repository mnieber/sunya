import typing as T

from kits.python_app.impl.namespace import PythonModule, Rule


class Runtime(PythonModule):
    class Rules:
        class GetIgnorePatterns(Rule):
            class Args:
                default_ignore: bool
                extra_ignore: T.List[str]

            class Returns:
                ignore_patterns: T.List[str]
