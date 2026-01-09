# Instructions for writing Python files

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

Although the standard Python library has a dataclasses package, I prefer the one from the dataclassy pypi package. Therefore, whenever I mention dataclasses, I mean the ones from dataclassy. Remember that in dataclassy it's allowed to initialize a dict field using `= {}` and a list field using `= []`.
