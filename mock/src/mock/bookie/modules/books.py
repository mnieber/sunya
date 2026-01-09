from kits.python_app.impl.namespace import PythonModule
import typing as T

from sunya import Entity

if T.TYPE_CHECKING:
    from .chapters import Chapters  # noqa: F401


class Books(PythonModule):
    class Models:
        class Book(Entity):
            title: str
            chapters: T.List["Chapters.Models.Chapter"] = []
