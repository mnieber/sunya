# Instructions for writing backend module specs

Taking the roadmap.md file as input, your task is to identify which backend module specification files (aka backend module specs) are needed, and to generate these module specs.

When writing a backend module spec, please follow the example in the backend/modules/blogs.py file. This example should be followed closely in terms of the syntax and structure that it proposes. However, you have a lot of freedom to decide which code-units you add to the module spec (as long as you adhere to the prescribed structure and syntax). It's recognized that the problem of mapping the roadmap to the module spec is not well-defined, and that many alternative solutions are possible, so just do your best to come up with one possible solution.

## Purpose of a backend module spec

The purpose of the backend module spec is to give a high-level description of the backend code-units that are defined in a particular module. The module spec does not describe use-cases, as these are described in the scenarios (that instantiate these mock code-units as so-called actors).

## Top-level module class

The top-level data-structure is a so-called module class that inherits from Module. It acts as a namespace for all mock code-units for a specific module.

### Django models

The Models section of the module class describes the Django models that are based on the entities in the roadmap

### Actions

The Actions section describes the action functions. An action function is a function that changes the state (typically the database-state) of the application. You can think of the action functions as the "mutation-api" of the module. If the roadmap describes an operation that involves a state-change, you will probably need to specify an action function for it.

### Api views

The Api section describes the api views.

### Enums

The Enums section describes the enums that are referenced in the Models section.

### Domain events

The DomainEvents section describes the domain events that would be interesting to send from the action functions.
The purpose of domain events is to inform external observers about what is going on in the system.

## Instantiation of mock objects

Following the module class, the module spec creates instances of global singleton mock objects. These are mock objects for which there exists only one instance. They are instantiated in the module spec so that all scenarios can use them just by importing them. For example, since the create_blog_action is a global function, and since all scenarios can use it, it is instantiated in this section of the module spec.

When I ask you to write a module spec, please also consider which actors (that are based on the mock code-units in the module spec) will be needed in the current scenarios, and create these actors in the module spec file.

## The actor_to_str functions

In this section of the module spec, we define instances of the actor_to_str multi-method for specific code-units that are defined in the module spec. The actor_to_str multi-method is used to convert any code-unit into a string that identifies that actor.

## Updating an existing module spec

When you need to update an existing module spec, please replace the existing code-units with one-line comments in your output. This makes it easier for me to copy-and-paste the new code-units.
