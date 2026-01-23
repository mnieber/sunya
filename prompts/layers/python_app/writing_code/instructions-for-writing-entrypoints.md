# Instructions for writing entrypoints

When writing an entrypoint file, please follow the example in `bookie/runtime/entrypoints/bookie.py`.

## Add entrypoints to pyproject.toml

As shown in bookie/pyproject.toml, entrypoints should be added to the `[project.scripts]` section of pyproject.toml.

## Parsing args

RULE: Please use a separate `_parse_args` function that is based on the argparse package.
