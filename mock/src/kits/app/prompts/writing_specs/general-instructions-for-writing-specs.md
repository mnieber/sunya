# General instructions for writing specs

## The process of creating technical specifications

The creation of a technical specification from the roadmap happens separately for the frontend and the backend.
Therefore, when I ask for your help in creating a technical specification, I will always mention if this is for the frontend or the backend.

The technical specification contains two sets of files:

- a set of module specification Python files
- a set of scenario Python scripts

The module specification files define mock code-units.
These mock code-units are referenced in the scenario to describe the implementation of a workflow in a roadmap milestone.

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
