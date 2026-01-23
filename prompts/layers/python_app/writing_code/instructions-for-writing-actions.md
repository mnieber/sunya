# Instructions for writing action files

When writing an action file, please follow the example in `bookie/books/actions/create_book.py`.

RULE: Each action function should be in its own file.

Action files live in the actions sub-directory. An action is a function that changes the application state. This contrasts actions from rules, which do not change the application state.

## Exceptions

An action should raise an exception if it cannot reach its goal. It doesn't return a success state (though it may return other types of results). Therefore, create_book raises an exception if num_chapters is too high.
