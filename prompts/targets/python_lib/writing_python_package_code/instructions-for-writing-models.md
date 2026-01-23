# Instructions for writing model files

When writing an model file, please follow the example in `bookie/books/models/book.py`.

Model files live in the models sub-directory.

RULE: By default, use a separate model file for each model, even if this results in a very small file.
RULE: An model is a class based on the `dataclass` type from the dataclassy package.
