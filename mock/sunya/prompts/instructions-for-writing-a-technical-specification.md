# Project description

At my company, we have a software development process that contains three steps:

- first, we create a roadmap
- from this roadmap, we create a technical specification
- from this technical specification, we create software

I need your help with the step of creating the technical specifications from the roadmap. Below, I will give some details about the structure of these technical specifications.

## The process of creating technical specifications is divided into frontend and backend

As mentioned above, we create a technical specification from the roadmap. This happens separately for the frontend and the backend. Therefore, when I ask for your help in creating a technical specification, I will always mention if this is for the frontend or the backend.

## The technical specification

The technical specification contains two sets of files:

- a set of module specification Python files
- a set of scenario Python scripts

Both module specifications and scenario scripts are derived from the roadmap.md file. The roadmap contains milestones. A milestone describes a work-flow that refers to entities and processes that involve these entities. The work-flow in a milestone is translated to a scenario. The entities and processes that are mentioned in the work-flow are translated to code-units in one or more module specification files.

### The module specifications

The module specification files define various mock code-units. In case of a backend module spec these could be data-models, action functions, api-views, etc. It's important to note that these mock code-units are not going to be used in the actual software. They are merely empty stubs that allow us to describe the design at a high level. Instances of these stubs code-units are used in the scenario scripts to simulate the behaviour of the actual software. Together, the module specifications and the scenarios allow us to capture a high-level description of the application design, and to roughly estimate whether this design will be suitable.

A specific set of instructions for writing a module specifications will be made available in the reference data. When I ask you to write a module specification, please follow these specific intructions.

### The scenarios

The scenarios are Python scripts that instantiate the mock code-units. Please see the reference data for specific instructions on how to write the frontend and backend scenario scripts.

A specific set of instructions for writing a scenarios will be made available in the reference data. When I ask you to write a scenarios, please follow these specific intructions.

## Use of sample code

The specific instructions will always contain references to sample code. It's important that the structure of this sample code is followed closely when generating the requested code. If you cannot find the referenced sample code, please let me know.

The sample code is always based on the roadmap.md file. By studying the sample code and roadmap.md, you will be able to see how the information in the roadmap is used for generating module specifications and scenarios.
