# Instructions for mapping scenario specs to implementation

## Module namespaces to feature packages

Each module namespace referenced in the scenario specs implies a corresponding "feature package" (sub-package directory) in the application.

**Example:** A scenario spec referencing `c.Books.Actions.CreateBook` implies that the application has a `bookie/books/` feature package directory.

If the application is called `bookie`, then:

- The `Books` namespace → `bookie/books/` feature package
- The `Chapters` namespace → `bookie/chapters/` feature package
- Etc.

## Mapping of specs onto filenames and function names

RULE: Please inspect the example code and example spec_src to understand how the modules that are described in the specs are mapped onto source code files.

Note that usually each source code file is focussed on one particular function or class (plus helper functions). Group files (that group a family of related functions or classes) are used rarely.

## Validation

You don't need to validate that implementation matches specs, I will do this myself. If you think something is missing in the spec then please delay code generation and ask me to clarify it.
