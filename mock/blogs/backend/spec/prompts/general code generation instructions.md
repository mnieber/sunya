# General code generation instructions

## The scope of the code generation is limited to the backend

The code generation instructions sometimes mention the frontend to clarify the workflow. However, we will only generate the code for the backend.

## Use of specific code generation instructions relevant to the code unit

When I ask you to write the source code for a code unit (such as an api view), then a specific set of instructions for writing such a code unit will be available. If you cannot find the specific instructions, please let me know.

## Use of sample code

The specific instructions will always contain references to sample code. It's important that this sample code is followed closely when generating the requested code. If you cannot find the referenced sample code, please let me know.

The sample code is always based on the spec/backend/modules/blogs.md spec file. By studying the sample code and blogs/spec.md, you will be able to see how the information in a module spec is used for generating a specific source file.

## Use of dataclassy

Although the standard Python library has a dataclasses package, I prefer the one from the dataclassy pypi package. Therefore, whenever I mention dataclasses, I mean the ones from dataclassy.

## Updating existing source files

When you need to update an existing source file, please replace the existing code-blocks with one-line comments in your output. This makes it easier for me to copy-and-paste the new code-blocks.

## Use of spec files for code generation

Code generation is also informed by module spec files. When I ask you to write source code, please find out what the relevant module spec files are, and ask questions if you think something in the spec files is unclear or missing.

## Scenario descriptions

Code generation is also informed by scenario descriptions. A scenario will mention actors (i.e. the objects in the scenario) that are based on the models in the spec files. When I ask you to write source code, please find out what the relevant scenario files are, and use this information to implement the right behaviour in the source code.

The actors in scenarios are described using a special notation: [(actor name+)(actor sub-type):actor-type].
For example:

- the notation `hello-world+:blog-post` means that the type is `blog-post` and the name is `hello-world`.
- the notation `wow+special:blog-post` means that the type is `special:blog-post` and the name is `wow`.

For each step, the scenario will show how the actors are changed by the step. It's important to note that it shows the state of the actors after the entire step - including its sub-steps - has completed. This means that if the top-level step tells us that actor1.foo was changed to "bar", then it's possible that this change only happened in the last sub-step that is included in the high-level step.

## Roadmap description

Finally, code generation is also informed by a roadmap. The roadmap describes milestones that are similar to scenarios, but more high-level. You can think of the scenarios as technical break-downs of these milestones. If the scenarios contradict the roadmap, please let me know.
