# Instructions for mapping module specs to implementation

## Module specs to feature packages

Each module specification implies a corresponding "feature package" (sub-package directory) in the application.

**Example:** The `modules/books.py` module spec implies that the application has a `bookie/books/` feature package directory.

If the application is called `bookie`, then:

- The `Books` module spec → `bookie/books/` feature package
- The `Chapters` module spec → `bookie/chapters/` feature package
- Etc.

## Mapping of specs onto filenames and function names

RULE: Convert the spec section name to snake_case for the file/function name. For example, the Books.Actions.CreateBook action implies the books/actions/create_book.py filename with a create_book function.

## RULE: In general use one file per model, action, rule or util.

For example, `bookie/books/actions/create_book.py` contains the `create_book` action, and `bookie/books/models/book.py` contains the `Book` model.
