import lorem
import mock.bookie.backend.namespace as B
from sunya import R as r, G as g, match_step as match, it


def implement_step(step):
    if match(step, it().creates_the(r.book)):
        r.book = B.Books.Models.Book(title="My Book")

    elif match(
        step, it().calls_the(g.create_chapter_action).to_create_the(r.current_chapter)
    ):
        r.current_chapter = B.Chapters.Models.Chapter(title=f"Chapter {lorem.word()}")

    elif match(step, it().creates_a(r.paragraph).for_the(r.current_chapter)):
        r.current_chapter.paragraphs.append(lorem.paragraph())
