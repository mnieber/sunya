# Instructions for writing backend scenario files

When writing the backend scenario file for a milestone in the roadmap, please follow the example in the blogs/backend/scenarios/ms1_a_user_creates_a_blog/scenario.py file.

## Scenarios are executable code that result in a `trace` artifact

As mentioned elsewhere, scenarios are purely declarative. However, it's possible to execute a scenario script and thus similate the behaviour of the actual applicaton. As the simulation is executed, handler functions are triggered that build a a trace of the simulation in memory, that shows the evolution of the application state over time, which can be saved to a yaml file. These yaml files can can be loaded into a viewer, thus allowing us to turn scenarios into web-pages that can be inspected by anyone who is interested in exploring the different scenarios.

## Scenarios can declare goals and steps

When a goal is declared during a scenario, a special handler function is triggered that adds the goal to the scenario `trace`. Within a goal, the function may declare a step. In that case, a handler is triggered that adds the step to the same `trace`.

### Actors are created for any mentioned global resources

When a step is declared that mentions global resources then the `resolve_entity_in_global_namespace` handler is triggered. This handler tries to match the resource name with a set of known resource names. If a pattern matches, then a mock code-unit (from one of the module specs) is instantiated and stored in the global namespace. Global resources are singletons which are only instantiated once.

### Actors are created in the `implement_step` handler

Similarly, when a step is declared then the `implement_step` handler is triggered. This handler tries to match the step with a set of known patterns. If a pattern matches, then the corresponding actors are instantiated (again, using the mock code-units in the module specs) or mutated. For example, if a scenario step describes how the user renames a blog, then a handler may be triggered that updates the name field on the corresponding actor. When the scope of the step function is exited then it detects the changes in the actors. In this way, by running the scenario, we can collect informations about how the actors are mutated in each step.

## The start function

The start function creates the scenario instance. This scenario instance is automatically added to a store, so that the caller of the scenario can later extract the information that was generated during the scenario.
