# Instructions for writing backend scenario files

When writing the backend scenario file for a milestone in the roadmap, please follow the example in the blogs/backend/scenarios/ms1_a_user_creates_a_blog.py file.

Taking the roadmap.md file as input, your task is to write a backend scenario script for each milestone in the roadmap.

## Purpose of a backend scenario

The purpose of a backend scenario is to document and communicate the use-cases that the backend must support to the backend development team. This fits into the overarching task of creating the complete specification of the full application.

### Relationship to the frontend scenarios

Note that there also exist frontend scenarios that are used by the frontend team. Both backend scenarios and frontend scenarios are derived from the same roadmap. Backend scenarios may refer to actors that come from frontend module specs, for example to explain the work-flow that leads to an api call made to the backend. However, although references are sometimes made to what happens in the frontend, the focus of the backend scenario is to describe what happens in the backend.

## The run function

The entry-point for the scenario is the run function. If the scenario requires an actor that is not created by the scenario itself, then it's created in the run function. The run function calls the start function to start the scenario.

## The start function

The start function creates the scenario instance. This scenario instance is automatically added to a store, so that the caller of the scenario can later extract the information that was generated during the scenario.

## The add_step function

The start function will create a scenario and then add steps to it using the add_step function. The steps in a scenario form a tree structure, where each step may contain child steps.

A step is a tuple that contains one or more actors (or roles, see below) and small strings that qualify the relationships between the actors. To add a child step to a step, we use the `with` keyword to create a child-step scope, and then call add_step within that scope.

### The StepBuilder

It's also possible to add a step using the StepBuilder class. This allows for a more concise syntax, that starts with the magical the() function. This function let's you write things such as the(foo).has_an_internal(bar).with_a(baz). This gets translated into the following step: ("the", foo, "has an internal", bar, "with a", baz).

## The add_goal function

It's often useful to specify to which goal a sub-tree of steps contributes. This is done with the add_goal function, that works similar to the add_step function.

## Actors

The steps and goals in a scenario can refer to actors. Each scenario function can create an actor by instantiating a code-unit that is defined in a module spec. When the actor has been created, the scenario function calls the add_actor function to register it - under a given name - with the scenario.

### The global namespace object

Once an actor has been registered, it can be retrieved via the special 'G' object that acts as a global namespace. This global namespace will look up symbols first inside of the current scenario, and then it its global registry. The global registry contains global actors that are instantiated in the module specs.

## Mutation of actors

Within a certain step, the scenario function can also mutate an actor. For example, if the scenario describes how the user renames a blog, then the scenario function may update the name field on the corresponding actor. Note that the actor is mutated, rather than creating a new updated actor. The add_step function is able to detect the changes in the actor when its associated scope is exited. In this way, by running the scenario, we can collect informations about how the actors are mutated in each step.

# Roles

Instead of referring to an actor, a step may also refer to a role. This allows the step to be more generic, as it can refer to a "possible actor" that has not yet been defined. The scenario can create roles using the add_role function. When the scenario calls add_actor then it can specify the role that this actor will perform. This approach allows us to build a rich data-structure that enables the navigation from a particular actor in a particular step to its role within that step, and from there to other steps that refer to the same role.
