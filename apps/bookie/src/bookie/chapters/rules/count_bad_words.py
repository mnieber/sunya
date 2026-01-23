import logging

logger = logging.getLogger(__name__)


def count_bad_words(paragraph: str) -> int:
    """
    Count the number of bad words in a paragraph.

    A bad word is defined as any word that contains the letter 'a' or 'b'.

    Args:
        paragraph: The text to analyze

    Returns:
        The count of bad words (words containing 'a' or 'b')
    """
    words = paragraph.split()
    bad_word_count = 0

    for word in words:
        # Check if the word contains 'a' or 'b' (case-insensitive)
        if 'a' in word.lower() or 'b' in word.lower():
            bad_word_count += 1

    return bad_word_count


def filter_bad_words(paragraph: str, max_bad_words: int) -> str:
    """
    Remove words from the paragraph to ensure no more than max_bad_words remain.

    Words are removed from the end of the paragraph until the bad word count
    meets the limit.

    Args:
        paragraph: The text to filter
        max_bad_words: Maximum number of bad words allowed

    Returns:
        The filtered paragraph with bad words removed to meet the limit
    """
    words = paragraph.split()

    # If we're already under the limit, return the paragraph as-is
    if count_bad_words(paragraph) <= max_bad_words:
        return paragraph

    # Build a new paragraph by removing words until we meet the limit
    filtered_words = []
    bad_word_count = 0

    for word in words:
        is_bad_word = 'a' in word.lower() or 'b' in word.lower()

        # Only add the word if we haven't exceeded the bad word limit
        if is_bad_word:
            if bad_word_count < max_bad_words:
                filtered_words.append(word)
                bad_word_count += 1
        else:
            filtered_words.append(word)

    return ' '.join(filtered_words)
