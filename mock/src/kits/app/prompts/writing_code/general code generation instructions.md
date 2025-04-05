# General code generation instructions

## The scope of the code generation is either the backend or the frontend

The code generation instructions sometimes mention both the frontend and the backend. However, when I ask you to generate code, it's always for either the backend or the frontend, never for both simultaneously.

## Code is written step by step

The process of generating code together should be stepwise. When writing backend code, the steps are as follows:

1. First you will review the instructions and tell me if they are clear. If something is underspecified, please ask me about it.
2. Next, if there is an entrypoint to be generated, we will generate that entrypoint
   - This entrypoint will depend on models and actions that do not yet exist, so the imports will fail. However, that's okay for now.
3. Next, we will write the first `models` files, up to the point where we are able to implement the first action.
4. Next, we implement the first `action` file.
5. We repeat this process until all code has been generated.

## Generate just one file at a time!

Please always generate just one file at a time. This is very important! This allows us to check each file and iterate on it before we move on.
In the rare cases that I would like you to generate multiple files at once, then I will explicitly ask you to do so.

## Ignore broken imports

If the generated file contains imports to symbols that do not yet exist, then don't worry about it, as we will generate these
related files later.

## Use of specific code generation instructions relevant to the code unit

When I ask you to write the source code for a code unit (such as an api view), then a specific set of instructions for writing such a code unit will be available. If you cannot find the specific instructions, please let me know.

## Use of sample code

The specific instructions will always contain references to sample code. It's important that this sample code is followed closely when generating the requested code. If you cannot find the referenced sample code, please let me know.

The sample code is always based on spec files that are also provided. By studying the sample code and the example spec files, you will be able to see how the information in the spec files is used for generating a specific source file.

## Use of comments

Functions, classes and files should not have a "header" comment at the top, nor should they have a docstring.
Inline comments in the code are welcome, but don't add comments for things that are already obvious from reading the code.
Rather, use comments to broadly outline the steps that are taken in the function, grouping related lines of code below a comment that announces the step.

## Use of logging

Please use the `logging` package for producing progress messages and error/warning messages. The print statement statement should only be used for the actual application output. Use `logger.info` when running with the verbose option. We'll use `logger.debug` when the running with the "double verbose" option. I might add `logger.debug` manually myself, but don't put `logger.debug` in the generated code. Use `logger.warning` if there are warnings that the user should definitely fix (otherwise, use `logger.info`). Use `logger.error` when appropriate.

## Use of dataclassy

Although the standard Python library has a dataclasses package, I prefer the one from the dataclassy pypi package. Therefore, whenever I mention dataclasses, I mean the ones from dataclassy.

## Updating existing source files

When you need to update an existing source file, please replace the existing code-blocks with one-line comments in your output. This makes it easier for me to copy-and-paste the new code-blocks.

## Kits are ignored for code generation

The `kits` support us in translating the roadmap into spec files. They are not relevant for the code generation process.
