import logging
import lorem

from bookie import settings
from bookie.chapters.rules.count_bad_words import count_bad_words, filter_bad_words

logger = logging.getLogger(__name__)


def create_paragraph() -> str:
    """
    Create a paragraph with lorem ipsum text.

    The paragraph is filtered to ensure it contains no more than
    MAX_BAD_WORDS_PER_PARAGRAPH bad words (words containing 'a' or 'b').

    Returns:
        A filtered paragraph string
    """
    # Generate lorem ipsum text
    paragraph = lorem.paragraph()

    # Count bad words
    bad_word_count = count_bad_words(paragraph)
    logger.debug(f"Generated paragraph with {bad_word_count} bad words")

    # Filter the paragraph to meet the maximum bad word limit
    filtered_paragraph = filter_bad_words(
        paragraph,
        settings.MAX_BAD_WORDS_PER_PARAGRAPH
    )

    final_bad_word_count = count_bad_words(filtered_paragraph)
    logger.debug(f"Filtered paragraph now has {final_bad_word_count} bad words")

    return filtered_paragraph
