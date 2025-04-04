# General code generation instructions

## The scope of the code generation is either the backend or the frontend

The code generation instructions sometimes mention both the frontend and the backend. However, when I ask you to generate code, it's always for either the backend or the frontend, never for both simultaneously.

## Use of specific code generation instructions relevant to the code unit

When I ask you to write the source code for a code unit (such as an api view), then a specific set of instructions for writing such a code unit will be available. If you cannot find the specific instructions, please let me know.

## Use of sample code

The specific instructions will always contain references to sample code. It's important that this sample code is followed closely when generating the requested code. If you cannot find the referenced sample code, please let me know.

The sample code is always based on spec files that are also provided. By studying the sample code and the example spec files, you will be able to see how the information in the spec files is used for generating a specific source file.

## Use of dataclassy

Although the standard Python library has a dataclasses package, I prefer the one from the dataclassy pypi package. Therefore, whenever I mention dataclasses, I mean the ones from dataclassy.

## Updating existing source files

When you need to update an existing source file, please replace the existing code-blocks with one-line comments in your output. This makes it easier for me to copy-and-paste the new code-blocks.
