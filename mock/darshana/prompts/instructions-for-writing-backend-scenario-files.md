# Instructions for writing backend scenario files

When writing the backend scenario file for a milestone in the roadmap, please follow the example in the blogs/backend/scenarios/ms1_a_user_creates_a_blog.py file.

Taking the roadmap.md file as input, your task is to write a backend scenario script for each milestone in the roadmap.

## Purpose of a backend scenario

The purpose of a backend scenario is to document and communicate the use-cases that the backend must support to the backend development team. The task of writing backend scenarios fits into a greater overarching task of creating the complete specification of the full application. For this reason, there also exist frontend scenarios that are used by the frontend team.

Both backend scenarios and frontend scenarios are derived from the same roadmap. Moreover, backend scenarios may refer to actors that come from frontend module specs, for example to explain the work-flow that leads to an api call made to the backend. Although actors based on frontend mock code-units (defined in frontend module specs) may appear in a backend scenario, the focus of the scenario is to describe what happens in the backend.

## The run function

The entry-point for the scenario is the run function. If the scenario requires an actor that is not created by the scenario itself, then it's created in the run function. The run function calls the start function to start the scenario.

## The start function

The start function creates the scenario instance. This scenario instance is automatically added to a store, so that the caller of the scenario can extract the information that was generated during the scenario.

## Scenario functions and the add_step function

The start function is also the first so-called scenario function. Each scenario function will add steps to the scenario, either directly or by calling other scenario functions. The steps in a scenario form a tree structure, where each step can contain child steps.

To add a step, the scenario function uses the add_step function. A step is a tuple that contains one or more actors and small strings that qualify the relationships between the actors. To add a child step to a step, we use the `with` keyword to create scope, and then call add_step within that scope.

### The StepBuilder

It's also possible to add a step using the StepBuilder class. This allows a more concise syntax, that starts with the magical the() function. This function let's you write things such as the(foo).has_an_internal(bar).with_a(baz). This gets translated into the following step: ("the", foo, "has an internal", bar, "with a", baz).

## The add_goal function

It's often useful to specify to which goal a sub-tree of steps contributes. This is done with the add_goal function, that works similar to the add_step function.

## Actors

The steps and goals in a scenario can refer to actors. Each scenario function can create an actor by instantiating a code-unit that is defined in a module spec. When the actor has been created, the scenario function calls the register function to register it - under a given name - with the scenario.

A scenario function can also use the global actors that are instantiated in the module specs. The global actors are added to a special 'g' object that acts as a namespace. Typically, the global actors are not registered with a scenario.

### The preregister function

In some cases, a step makes reference to an actor that has not yet been created. In that case it can use the preregister function to create a place-holder actor. When the real actor is created and registered, the scenario function will also pass in the placeholder actor to the register function, so that existing steps can be updated to replace the place-holder actor with the real actor.

## The register function

The register function is used to register an actor - under a given name - with the scenario. If an entity with the given name already exists in the scenario, then it will raise an exception. To prevent this from happening (for example, when creating entities in a for-loop) you can unregister the existing entity first. Note that unregister is a no-op if called with a preregistered entity.

## The get_entities() function

The magical get_entities() function returns a EntityLookup object that looks up entities in the current scenario. For example, if e = get_entities(), then e.foo will look up the entity in the scenario that has been registered with name "foo". If scenario doesn't have an entity for the given name, then a new preregistered entity will be created for that name.

## Mutation of actors

Within a certain step, the scenario function can also mutate the actor. For example, if the scenario describes how the user renames a blog, then the scenario function may update the name field on the corresponding actor. Note that the actor is mutated, rather than creating a new updated actor. The add_step function is able to detect the changes in the actor when its associated scope is exited. In this way, by running the scenario, we can collect informations about how the actors mutate in each step.
