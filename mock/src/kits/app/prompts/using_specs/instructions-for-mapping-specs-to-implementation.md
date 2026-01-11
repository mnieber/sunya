# Instructions for mapping module specs to implementation

## Module specs to feature packages

Each module specification implies a corresponding "feature package" (sub-package directory) in the application.

**Example:** The `modules/books.md` module spec implies that the Python application has a `books/` feature package directory.

If the application is called `bookie`, then:

- The `Books` module spec → `bookie/books/` feature package
- The `Chapters` module spec → `bookie/chapters/` feature package
- The `Users` module spec → `bookie/users/` feature package

## Module spec sections to files and directories

The different sections within a module spec correspond to sub-directories and files within the related feature package.

**Mapping rules:**

- `Books.Models.Book` → `bookie/books/models/book.py` file containing a `Book` class
- `Books.Enums.BookStatuses` → enum class in `bookie/books/enums.py` file
- `Books.Actions.DeleteBook` → `bookie/books/actions/delete_book.py` file containing a `delete_book` function
- `Books.Rules.CanDeleteBook` → `bookie/books/rules/can_delete_book.py` file containing a `can_delete_book` function
- `Books.EntryPoints.ListBooks` → `bookie/books/entry_points/list_books.py` file containing a `list_books` function

**General pattern:**

1. Convert the spec section name to snake_case for the file/function name
2. Place the file in the appropriate sub-directory based on the section type
3. For Models: one file per model class
4. For Enums: group related enums in a single `enums.py` file
5. For Actions/Rules/EntryPoints: one file per function

## Action return values and error handling

**Return values:**

- Actions may return a value if this is useful for the caller
- Common pattern: return the created/modified entity (e.g., `return book`)
- Some actions may return `None` if there's nothing meaningful to return

**Error handling:**

- Actions should generally either succeed or raise an exception
- Don't return success/failure booleans - use exceptions for errors
- Let exceptions propagate to the caller unless you have a specific reason to catch them
- Use appropriate built-in exceptions (`ValueError`, `FileNotFoundError`, etc.) or define custom exceptions

**Example patterns:**

```python
# Returns the created entity
def create_book(title: str, num_chapters: int) -> Book:
    book = Book(title=title)
    return book

# Returns None, modifies in place
def activate_user(user: User) -> None:
    user.is_active = True

# Raises exception on error
def delete_book(book_id: str) -> None:
    if not book_exists(book_id):
        raise ValueError(f"Book {book_id} not found")
    # ... delete logic
```
