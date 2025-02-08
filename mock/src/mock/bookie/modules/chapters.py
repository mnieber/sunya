from mock.django_app.namespace import Action
import typing as T

from sunya import Entity


class Chapters(PythonModule):
    class Models:
        class Chapter(Entity):
            title: str
            paragraphs: T.List[str]

    class Actions:
        class CreateChapter(Action):
            class Args:
                title: str
                num_paragraphs: int = 5

        class CreateParagraph(Action):
            class Args:
                length: str = "medium"  # short, medium, long
