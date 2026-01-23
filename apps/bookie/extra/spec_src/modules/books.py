import typing as T

from mock.entities.python_app.namespace import PythonPackage
from sunya import Entity

if T.TYPE_CHECKING:
    from .chapters import Chapters  # noqa: F401


class Books(PythonPackage):
    class Models:
        class Book(Entity):
            title: str
            chapters: T.List["Chapters.Models.Chapter"] = []

    class Settings:
        MAX_BAD_WORDS_PER_PARAGRAPH: int = 5
