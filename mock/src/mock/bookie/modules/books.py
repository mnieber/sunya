from kits.python_app.namespace import Action, PythonModule
import typing as T

from sunya import RelatedSet, Entity

if T.TYPE_CHECKING:
    from .chapters import Chapters  # noqa: F401


class Books(PythonModule):
    class Models:
        class Book(Entity):
            title: str
            chapters: RelatedSet["Chapters.Models.Chapter"] = []

    class Actions:
        class CreateBook(Action):
            class Args:
                title: str
                num_chapters: int = 3
                paragraphs_per_chapter: int = 5
