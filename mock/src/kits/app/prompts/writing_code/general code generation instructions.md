# General code generation instructions

## Please follow the rules very closely

In the instructions in the reference data, I will indicate the rules using a `RULE:` prefix.
It's extremely important to follow the rules as closely as possible. If the rules are not followed closely then I will have to manually edit the generated source files and upload them again, which will result in a very tedious process. This should be avoided at all cost.

## The scope of the code generation is either the backend or the frontend

The code generation instructions sometimes mention both the frontend and the backend. However, when I ask you to generate code, it's always for either the backend or the frontend, never for both simultaneously.

## Use of spec files for code generation

Code generation is informed by scenario spec files and module spec files. These spec files will be uploaded as a single text-file to the chat in which we collaborate on the code generation. When I ask you to write source code, please find out what the relevant spec files are, and ask questions if you think something in the spec files is unclear or missing.

A scenario will mention actors (i.e. the objects in the scenario) that are based on the models in the spec files. When I ask you to write source code, please find out what the relevant scenario files are, and use this information to implement the right behaviour in the source code.

## Use of specific code generation instructions relevant to the code unit

When I ask you to write the source code for a code unit (such as an api view), then a specific set of instructions for writing such a code unit will be available in the project instructions. If you cannot find the specific instructions, please let me know.

## Use of example code

The project instructions will always contain references to example code. It's important that this example code is followed closely when generating the requested code. If you cannot find the referenced example code, please let me know.

The example code is always based on the module specs and scenarios specs in the examples directory. By studying the example code and these example spec files, you will be able to see how the information in the spec files is used for generating a specific source file.
