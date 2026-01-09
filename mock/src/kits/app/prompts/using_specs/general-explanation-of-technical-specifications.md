# Project description

At my company, we have a software development process that contains three steps:

- first, we create a roadmap
- from this roadmap, we create a technical specification
- from this technical specification, we create software

When I ask for your help, it will be either with translating the roadmap into the specification files, or with generating the real app from the specification files. However, I will never ask you to help with both steps at the same time (the steps are strictly separate).

## The process of creating a roadmap

A roadmap contains a glossary and a list of milestones. A milestone describes a work-flow that refers to actors, resources and processes that involve these actors and resources.
The blogs/roadmaps/roadmap.md file gives an example of a roadmap. From this example, it will be obvious how they are structured and how you can help with the creation of new roadmaps.

### The module specifications

The module specification files define various data-structures. A scenario spec may also (implicitly) define a code-unit in the module spec. E.g. the scenario spec may refer to Users.Actions.DeleteUser, which means that the Users module has a DeleteUser action function.

### The scenarios

The scenarios are Markdown files (generated from Python scripts) that reference the module spec.
