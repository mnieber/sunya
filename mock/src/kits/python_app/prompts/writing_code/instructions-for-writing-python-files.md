# Instructions for writing Python files

## Code is written step by step

The process of generating code together should be stepwise. When writing backend code, the steps are as follows:

1. First you will review the instructions and tell me if they are clear. If something is underspecified, please ask me about it.
2. Next, if there is an entrypoint to be generated, we will generate that entrypoint
   - This entrypoint will depend on models and actions that do not yet exist, so the imports will fail. However, that's okay for now.
3. Next, we will write the first `models` files, up to the point where we are able to implement the first action.
4. Next, we implement the first `action` file.
5. We repeat this process until all code has been generated.

## Generate just one file at a time!

RULE: Always generate just one file at a time.

This is very important! It allows me to check each file and iterate on it before we move on.
In the rare cases that I would like you to generate multiple files at once, then I will explicitly ask you to do so.

## Ignore broken imports

If the generated file contains imports to symbols that do not yet exist, then don't worry about it, as we will generate these
related files later.

## Use of comments

RULE: Functions, classes and files should not have a "header" comment at the top, nor should they have a docstring.

Inline comments in the code are welcome, but don't add comments for things that are already obvious from reading the code.
Rather, use comments to broadly outline the steps that are taken in the function, grouping related lines of code below a comment that announces the step.

## Use of logging

Please use the `logging` package for producing progress messages and error/warning messages.

RULE: The print statement statement should only be used for the actual application output.

Use `logger.info` when running with the verbose option. We'll use `logger.debug` when the running with the "double verbose" option.
Use `logger.warning` if there are warnings that the user should definitely fix (otherwise, use `logger.info`). Use `logger.error` when appropriate.
I might add `logger.debug` manually myself, but don't put `logger.debug` in the generated code.

## Use of dataclassy

Although the standard Python library has a dataclasses package, I prefer the one from the dataclassy pypi package. Therefore, whenever I mention dataclasses, I mean the ones from dataclassy.
