from kits.django_app.namespace import Action
import typing as T

from sunya import Entity


class Filemaps(PythonModule):
    class Models:
        class FilemapNode(Entity):
            target_path: str
            # Source files are read from this path
            source_path: str
            # List of filenames relative to the source_path
            filenames: T.List[str]
            child_nodes: T.List["Filemaps.Models.FilemapNode"] = []

    class Actions:
        class CopyFiles(Action):
            pass
            # The return type is the list of destination filenames

        class PurgeFiles(Action):
            pass
            # Receives, among other args, the list of copied_files

    class Rules:
        pass
