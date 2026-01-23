from mock.entities.python_app.namespace import PythonModule
import typing as T

from sunya import Entity


class Chapters(PythonModule):
    class Models:
        class Chapter(Entity):
            title: str
            paragraphs: T.List[str]
