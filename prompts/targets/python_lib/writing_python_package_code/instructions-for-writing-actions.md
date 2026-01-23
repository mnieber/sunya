# Instructions for writing action files

When writing an action file, please follow the example in `bookie/books/actions/create_book.py`.

Each action function should be in its own file.

Action files live in the actions sub-directory. An action is a function that changes the application state as required by a particular "role". Here "role" is meant in the context of SRP, for example: the "books manager" could conceptually be a role in our system, and the create_book action is responsible to that role.
