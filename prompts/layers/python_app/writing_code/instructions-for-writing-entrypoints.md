# Instructions for writing entrypoints

When writing an entrypoint file, please follow the example in `bookie/runtime/bookie.py`. When a pyproject file exists, then entrypoints should be added to its `[project.scripts]` section.

## Parsing args

RULE: Please use a separate `_parse_args` function that is based on the argparse package.
