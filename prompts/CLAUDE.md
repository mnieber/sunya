This file describes how the prompts directory is used to guide the source code generation.

# The prompts/targets directory

In the targets directory you will find the instructions for generating the code for different types of applications, such as a django app or a react app. Each target refers to a combination of layers that explains how to generate the code for a particular technology (e.g. python_lib) that is used in the target.

Each target has an index.md file that is the starting point for understanding how to generate code for that target.

# The prompts/layers directory

In the layers directory you will find the instructions for generating the code for a particular technology (e.g. python_lib).

Each layer has an index.md file that is the starting point for understanding how to generate code for that layer. Moreover, each layer has a skills directory. A skill describes how to implement a particular pattern or solution within the layer. For example, in the python_lib layer we have a skill that explains how to write a settings.py file for our python library.

# The prompts/examples directory

Targets and layers will refer to example code that lives in the examples directory.
