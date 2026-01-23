import typing as T

from mock.entities.python_app.namespace import PythonPackage
from sunya import Entity


class Chapters(PythonPackage):
    class Models:
        class Chapter(Entity):
            title: str
            paragraphs: T.List[str]

    class Rules:
        class IsBadWord:
            """
            Returns True for a word that - after stripping the prefix of "aaa" -
            contains the letter 'a' or 'b'.
            """

    class Enums:
        class TitleStyles:
            NORMAL: str = "normal"
            EXCLAMATIONS: str = "exclamations"

    class Forms:
        class CreateChapterForm:
            title: str
            nr_of_paragraphs: int
            title_style: "Chapters.Enums.TitleStyles"

    class Utils:
        class StripPrefix:
            pass
