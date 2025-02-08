from mock.django_app.namespace import Action
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
                description: T.Optional[str] = None
                num_chapters: int = 3
                paragraphs_per_chapter: int = 5
