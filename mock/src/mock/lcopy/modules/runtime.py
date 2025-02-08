import typing as T

from sunya import Entity, JSON


class Runtime(PythonModule):
    class Types:
        class Options(Entity):
            configs: JSON
            destination: str
            labels: T.List[str]
            conflict: str
            verbose: bool
            purge: bool
            dry_run: bool

    class Actions:
        pass

    class Rules:
        pass
