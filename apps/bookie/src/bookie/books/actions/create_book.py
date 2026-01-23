import logging

import bookie.settings as settings
import lorem
from bookie.books.models.book import Book
from bookie.chapters.actions.create_chapter import CreateChapterForm, create_chapter

logger = logging.getLogger(__name__)


def create_book(
    title: str,
    num_chapters: int = 3,
    paragraphs_per_chapter: int = 5,
) -> Book:
    """
    Create a book with the specified parameters.

    Args:
        title: The book title
        num_chapters: Number of chapters to create
        paragraphs_per_chapter: Number of paragraphs per chapter

    Returns:
        The created Book instance
    """
    book = Book(title=title)

    if num_chapters > settings.MAX_CHAPTERS_PER_BOOK:
        raise TooManyChaptersError(
            f"Cannot create book with {num_chapters} chapters. "
            f"Maximum allowed is {settings.MAX_CHAPTERS_PER_BOOK}."
        )

    # Create the specified number of chapters
    for i in range(num_chapters):
        # Prepare the create_chapter_form
        create_chapter_form = CreateChapterForm(
            title=f"Chapter {i+1}: {lorem.sentence()}",
            nr_of_paragraphs=paragraphs_per_chapter,
        )

        # Create the chapter
        chapter = create_chapter(book=book, create_chapter_form=create_chapter_form)
        book.chapters.append(chapter)

    return book


class TooManyChaptersError(Exception):
    pass
