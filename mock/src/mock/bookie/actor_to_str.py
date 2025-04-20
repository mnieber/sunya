from sunya import actor_to_str
import mock.bookie.namespace as B


@actor_to_str.method((B.Books.Models.Book,))
def book_to_str(book):
    return f"{book.title}+:book"


@actor_to_str.method((B.Chapters.Models.Chapter,))
def chapter_to_str(chapter):
    return f"{chapter.title}+:chapter"
