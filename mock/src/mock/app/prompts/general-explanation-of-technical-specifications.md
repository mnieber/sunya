# Project description

At my company, we have a software development process that contains three steps:

- first, we create a roadmap
- from this roadmap, we create a technical specification (mock app)
- from this technical specification, we create software (real app)

The technical specification is called the "mock app" because the specification files are themselves executable source
code that can be used to simulate the real application. These specification files describe the behaviour of the
real application, and therefore guide the generation of the real application code.

When I ask for your help, it will be either with translating the roadmap into the specification files (or mock app),
or with generating the real app from the specification files. However, I will never ask you to help with both steps
at the same time (the steps are strictly separate).

## Kits

The real application consists of modules that are roughly grouped in `backend` and `frontend`.
Because the mock application describes the real application, the same holds true for the mock app.

The work on a particular module is supported by so-called `kits`.
A `kit` is a collection of resources that allow us to write the spec files and then use them to generate the source code of the real app.
The kit supports this as follows:

- it contains a `write_specs` directory to explain how to write a certain type of module specs, e.g. for a django-app.
- it contains a `write_code` directory that explains how such module specs should be turned into source code
- it contains mock code-units that we can use when writing the module specs.

The following kits are available:

- The `app` kit can be used for any module.
- The `python_app` kit can be used for any Python module.
  - Spec examples for this kit are provided in the `instructions/examples/specs/bookie` directory
  - Real code examples for this kit are provided (if applicable) in the `instructions/examples/code/bookie` directory
- The `django_app` kit can be used for Django backend modules
  - Spec examples for this kit are provided in the `instructions/examples/specs/blogs/backend` directory
  - Real code examples for this kit are provided (if applicable) in the `instructions/examples/code/blogs_be` directory
- The `react_app` kit can be used for React frontend modules
  - Spec examples for this kit are provided in the `instructions/examples/specs/blogs/frontend` directory
  - Real code examples for this kit are provided (if applicable) in the `instructions/examples/code/blogs_fe` directory

Sometimes, these instructions of different kits overlap. For example, a django backend may use both the django_app kit and the python_app kit.
In case of overlap, please interpret the more specific instructions (e.g. of the django_app kit) as an extension of
the more general kit (e.g. python_app).

## The process of creating a roadmap

A roadmap contains a glossary and a list of milestones.
A milestone describes a work-flow that refers to actors, resources and processes that involve these actors and resources.
The blogs/roadmaps/roadmap.md file gives an example of a roadmap. From this example, it will be obvious how they are structured and how
you can help with the creation of new roadmaps.

## The process of creating technical specifications

The creation of a technical specification from the roadmap happens separately for the frontend and the backend.
Therefore, when I ask for your help in creating a technical specification, I will always mention if this is for the frontend or the backend.

The technical specification contains two sets of files:

- a set of module specification Python files
- a set of scenario Python scripts

The module specification files define mock code-units.
These mock code-units are referenced in the scenario to describe the implementation of a workflow in a roadmap milestone.

### The module specifications

The module specification files define various mock code-units. In case of a django_app these could be data-models, action functions, api-views, etc. It's important to note that these mock code-units are not going to be used in the actual software. They are merely empty stubs that allow us to describe the design at a high level. Instances of these stubs code-units are referenced in the scenario scripts to describe the behaviour of the actual software.

### The scenarios

The scenarios are Python scripts that reference the mock code-units.

### Scenarios are executable

The scenario scripts can be executed so that the behaviour of the actual software can be simulated. During the execution, there is a mechanism for triggering handler functions similar to how it's done in BDD with Cucumber. These handler funcions take care of instantiating or mutating the mock code-units that are referenced in the scenario script.

Note that executing the scenarios is not essential to the software development process. It's only a nice bonus. Just by reading a scenario, without executing it, a human or AI can gain a good understanding of how the actual software is supposed to behave.
