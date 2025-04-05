import logging
from bookie.chapters.models.chapter import Chapter
from bookie.chapters.actions.create_paragraph import create_paragraph

logger = logging.getLogger(__name__)


def create_chapter(title: str, num_paragraphs: int = 5) -> Chapter:
    chapter = Chapter(title=title)

    # Create the specified number of paragraphs
    for _ in range(num_paragraphs):
        paragraph = create_paragraph()
        chapter.paragraphs.append(paragraph)

    return chapter
