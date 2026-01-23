from mock.entities.python_app.namespace import PythonPackage
import typing as T

from sunya import Entity


class Chapters(PythonPackage):
    class Models:
        class Chapter(Entity):
            title: str
            paragraphs: T.List[str]

    class Rules:
        class CountBadWords:
            """
            Counts and filters bad words in a paragraph.

            A bad word is defined as any word that contains the letter 'a' or 'b'.
            """
            pass
