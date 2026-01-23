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

## Validation

You don't need to validate that implementation matches specs, I will do this myself. If you think something is missing in the spec then please delay code generation and ask me to clarify it.

## Quick Reference: Spec Sections to Implementation

| Spec Section               | Implementation Location                        | Example                    |
| -------------------------- | ---------------------------------------------- | -------------------------- |
| Books.Models.Book          | bookie/books/models/book.py (class)            | Book dataclass             |
| Books.Actions.CreateBook   | bookie/books/actions/create_book.py (function) | create_book() function     |
| Books.Forms.CreateBookForm | Co-located in action file (dataclass)          | In create_book.py          |
| Books.Rules.IsBadWord      | bookie/books/rules/is_bad_word.py (function)   | is_bad_word() function     |
| Books.Utils.StripPrefix    | bookie/books/utils/strip_prefix.py (function)  | strip_prefix() function    |
| Books.Settings.MAX\_\*     | bookie/settings.py (module-level constants)    | MAX_CHAPTERS_PER_BOOK = 10 |
| Books.Enums.TitleStyles    | bookie/books/enums.py (Enum class)             | TitleStyles(str, Enum)     |
