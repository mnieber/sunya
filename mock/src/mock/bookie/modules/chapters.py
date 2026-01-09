from kits.python_app.impl.namespace import PythonModule
import typing as T

from sunya import Entity


class Chapters(PythonModule):
    class Models:
        class Chapter(Entity):
            title: str
            paragraphs: T.List[str]
