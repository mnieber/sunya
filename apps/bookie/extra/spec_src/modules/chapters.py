from mock.entities.python_app.namespace import PythonPackage
import typing as T

from sunya import Entity


class Chapters(PythonPackage):
    class Models:
        class Chapter(Entity):
            title: str
            paragraphs: T.List[str]
