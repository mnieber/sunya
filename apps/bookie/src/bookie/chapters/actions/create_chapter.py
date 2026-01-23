import logging
from dataclassy import dataclass

from bookie.books.models.book import Book
from bookie.chapters.models.chapter import Chapter
from bookie.chapters.actions.create_paragraph import create_paragraph

logger = logging.getLogger(__name__)


@dataclass
class CreateChapterForm:
    """Form for creating a chapter."""
    title: str
    nr_of_paragraphs: int


def create_chapter(book: Book, create_chapter_form: CreateChapterForm) -> Chapter:
    """
    Create a chapter with the specified parameters.

    Args:
        book: The book to which this chapter belongs
        create_chapter_form: Form containing chapter creation parameters

    Returns:
        The created Chapter instance
    """
    chapter = Chapter(title=create_chapter_form.title)

    # Create the specified number of paragraphs
    for _ in range(create_chapter_form.nr_of_paragraphs):
        paragraph = create_paragraph()
        chapter.paragraphs.append(paragraph)

    return chapter
