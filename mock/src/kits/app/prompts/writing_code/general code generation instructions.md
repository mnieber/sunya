# Project description

The software development process contains three steps:

1. first, we create a roadmap
2. from this roadmap, we create a technical specification
3. from this technical specification, we create software

When I ask for your help, it will be either with translating the roadmap into the specification files, or with generating the real app from the specification files. However, I will never ask you to help with both steps at the same time (the steps are strictly separate).

## The process of creating a roadmap

A roadmap contains a glossary and a list of milestones. A milestone describes a work-flow that refers to actors, resources and processes that involve these actors and resources. The blogs/roadmaps/roadmap.md file gives an example of a roadmap. From this example, it will be obvious how they are structured and how you can help with the creation of new roadmaps.

## Please follow the rules very closely

In the instructions in the reference data, I will indicate the rules using a `RULE:` prefix.
It's important to follow the rules as closely as possible.

## Use of specific code generation instructions relevant to the code unit

When I ask you to write the source code for a code unit (such as an api view), then a specific set of instructions for writing such a code unit will be available in the project instructions. If you cannot find the specific instructions, please let me know.

## Use of example code

The project instructions will always contain references to example code. It's important that this example code is followed closely when generating the requested code. If you cannot find the referenced example code, please let me know.

The example code is always based on the module specs and scenarios specs in the examples directory. By studying the example code and these example spec files, you will be able to see how the information in the spec files is used for generating a specific source file.

# The specification files

## Use of spec files for code generation

Code generation is informed by scenario spec files and module spec files. When I ask you to write source code, please find out what the relevant spec files are, and ask questions if you think something in the spec files is unclear or missing.

## The specification files are written in Python and rendered to Markdown

During step 2, the specification files are written in Python since this allows us to use them programatically to create comprehensive project documentation. However, these Python files are rendered to Markdown (using the sunya tool) before they are used in step 3 to implement the specs. This is because the markdown documentation as it is simpler than the Python source code.

## The module specifications

The module specification files define various data-structures. A scenario spec may also (implicitly) define a code-unit in the module spec. E.g. the scenario spec may refer to Users.Actions.DeleteUser, which means that the Users module has a DeleteUser action function.

## The scenarios

The scenarios describe sequence diagrams that reference the module spec. The blogs/backend/scenarios/ms1_a_user_creates_a_blog/scenario.py gives an example of a backend scenario file for the first milestone in the example roadmap.

Scenarios can declare goals and steps. Steps are small actions that contribute to completing the workflow in a milestone. A goal describes a group of steps that work towards the same (intermediate) result. Steps are usually nested within a goal.

The scenario source code will use the actions namespace (`a`) to define the relation between the actors that participate in a step. The action namespace supports the following actions: `calls(*args, **kwargs)`, `creates(arg)`, `returns(arg)` and `rel(it().does_something_with(r.some_other_thing))`. The latter form is used for generic action descriptions.

Note that the scenario may refer to a `form` argument. This typically means that the actors (e.g. the target `book` instance) are passed as separate arguments, but the action values (e.g. the new book title and book status) are passed in a single object.
