# Project description

At my company, we have a software development process that contains three steps:

- first, we create a roadmap
- from this roadmap, we create a technical specification (mock app)
- from this technical specification, we create software (real app)

The technical specification is called the "mock app" because the specification files are themselves executable source code that can be used to simulate the real application. These specification files describe the behaviour of the real application, and therefore guide the generation of the real application code.

When I ask for your help, it will be either with translating the roadmap into the specification files (or mock app), or with generating the real app from the specification files. However, I will never ask you to help with both steps at the same time (the steps are strictly separate).

## The process of creating a roadmap

A roadmap contains a glossary and a list of milestones. A milestone describes a work-flow that refers to actors, resources and processes that involve these actors and resources.
The blogs/roadmaps/roadmap.md file gives an example of a roadmap. From this example, it will be obvious how they are structured and how you can help with the creation of new roadmaps.

### The module specifications

The module specification files define various mock code-units. In case of a django_app these could be data-models, action functions, api-views, etc. It's important to note that these mock code-units are not going to be used in the actual software. They are merely empty stubs that allow us to describe the design at a high level. Instances of these stubs code-units are referenced in the scenario scripts to describe the behaviour of the actual software.

### The scenarios

The scenarios are Python scripts that reference the mock code-units.

### Scenarios are executable

The scenario scripts can be executed so that the behaviour of the actual software can be simulated. During the execution, there is a mechanism for triggering handler functions similar to how it's done in BDD with Cucumber. These handler functions are defined in so-called impl directories and take care of instantiating or mutating the mock code-units that are referenced in the scenario script.

Note that executing the scenarios is not essential to the software development process. It's only a nice bonus. In fact, the impl directories are ignored when generating source code from spec files. Just by reading a scenario, without executing it, a human or AI can gain a good understanding of how the actual software is supposed to behave.
