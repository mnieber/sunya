# Instructions for writing entrypoints

When writing an action file, please follow the example in `bookie/__main__.py`.

## Parsing args

RULE: Please use a separate `_parse_args` function that is based on the argparse package.
