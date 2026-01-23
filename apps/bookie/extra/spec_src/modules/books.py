from mock.entities.python_app.namespace import PythonPackage
import typing as T

from sunya import Entity

if T.TYPE_CHECKING:
    from .chapters import Chapters  # noqa: F401


class Books(PythonPackage):
    class Models:
        class Book(Entity):
            title: str
            chapters: T.List["Chapters.Models.Chapter"] = []
