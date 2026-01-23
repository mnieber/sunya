# Instructions for writing action files

When writing an action file, please follow the examples in `bookie/books/actions/create_book.py` and `bookie/chapters/actions/create_chapter.py`.

RULE: Each action function should be in its own file.

Action files live in the actions sub-directory. An action is a function that changes the application state. This contrasts actions from rules, which do not change the application state.

## Exceptions

An action should raise an exception if it cannot reach its goal. It doesn't return a success state (though it may return other types of results). Therefore, create_book raises an exception if num_chapters is too high.

RULE: Prefer to define the exception class in the action file itself (very generic exception classes can be defined in utils/exceptions).

## Forms

RULE: If the action takes a form argument, then the related form is define in the action file that uses it.
RULE: This form argument will only contain simple values, not other entities. Therefore, in chapters/actions/create_chapter.py we see that the form does not contain the Book entity.

## RULE: Avoid comment header blocks

The CreateChapterForm class and create_chapter action are perfectly self-explanatory, therefore they have no header comment. The create_book action only has a comment to point out that it checks on the MAX_CHAPTERS_PER_BOOK settings, as this is not obvious from the outside.

## RULE: Start helper functions with an underscore

As shown in `bookie/chapters/actions/create_chapter.py`, the \_filter_paragraph helper function starts with an underscore.
