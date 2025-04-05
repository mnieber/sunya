import logging
import lorem
from bookie.books.models.book import Book
from bookie.chapters.actions.create_chapter import create_chapter

logger = logging.getLogger(__name__)


def create_book(
    title: str,
    num_chapters: int = 3,
    paragraphs_per_chapter: int = 5,
) -> Book:
    book = Book(title=title)

    # Create the specified number of chapters
    for i in range(num_chapters):
        chapter = create_chapter(
            f"Chapter {i+1}: {lorem.sentence()}", num_paragraphs=paragraphs_per_chapter
        )
        book.chapters.append(chapter)

    return book
