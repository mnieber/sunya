import typing as T

from sunya import Entity, JSON
from kits.python_app.entities import PythonModule


class Runtime(PythonModule):
    class Models:
        class Options(Entity):
            configs: JSON
            destination: str
            labels: T.List[str]
            conflict: str
            verbose: bool
            purge: bool
            dry_run: bool
            default_ignore: bool
            extra_ignore: T.List[str]

            def get_ignore_patterns(self):
                pass

    class Actions:
        pass

    class Rules:
        pass
