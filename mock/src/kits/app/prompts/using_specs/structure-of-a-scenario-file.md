# Structure of a scenario file

The blogs/backend/scenarios/ms1_a_user_creates_a_blog/scenario.py gives an example of a backend scenario file for the first milestone in the example roadmap.

## Purpose of a scenario

The purpose of a scenario is to document and communicate the use-cases that the application must support. This fits into the overarching task of creating the complete specification of the full application.

### Relationship between backend and frontend scenarios

Note that there usually exist both backend and frontend scenarios. Both are derived from the same roadmap. Although backend and frontend scenarios are mostly separate, it may happen that a backend scenarios refers to actors that come from frontend module specs, or vice versa, for example when describing the work-flow (in the frontend) that leads to an api call made to the backend. However, the main focus of a backend scenario is to describe what happens in the backend, and similar for frontend scenarios.

## Scenarios can declare goals and steps

Steps are small actions that contribute to completing the workflow in a milestone. A goal describes a group of steps that work towards the same (intermediate) result. Goals and steps may be nested.

## Steps describe facts

Every goal or step in a scenario contains a fact. A fact is a tuple that contains roles (such as `r.user`), global resources (such as `g.user_session`) and words that specify a relationship between the roles and global resources (e.g. `step("the", g.create_project_action, "creates_a", r.project, "that_is_owned_by_the", r.user)`).

A fact tuple can also be built using the `i` namespace. The previous tuple can be also written as `step(i.the(g.log_in_api_view).creates_a(g.user_session).for_the(r.user))`.

# The purpose of roles and global resources

You can think of global resources as singletons that can be used in any scenario. In contrast, you can think of roles as local variables within the scenario. During a scenario run, the same role may at various times point to different actors. Note that for practical reasons, roles _are_ in fact global (even though they are used as if they are local variables) so that a scenario can continue by using the roles declared in a previous scenario.

## Scenarios are declarative

The scenario does not describe how actors are created and assigned to roles. In the above example, it's implied that after completion of the step the `r.project` role refers to an instance of the `Projects.Models.Project` mock code-unit of the `Projects` backend module-spec. In other words, the scenario is purely declarative. It shows (or implies) how the software will behave, without describing the implementation of the behaviour. Within the scope of a step, the scenario may describe the expected application state using `assert` and `comment`, thus giving further insight into the application requirements.

## The run function

The entry-point for the scenario is the run function. The run function may set up the initial state by running a previous scenario. The run function calls the start function to start the scenario.

## Magical functions

### The the() function and anchors

The magical the() function creates a step that start with "the". This function let's you write things such as `the(foo).has_an_internal(bar).with_a(baz)` without the need to mention the `step` function explicitly. This is equivalent to writing the following step: `("the", foo, "has_an_internal", bar, "with a", baz)`. The argument of the `the()` function becomes the so-called anchor of the step. The anchor of a step can be referenced in the child-step using the `it()` function.

### The calls_the() clause

When a step contains a `calls_the` clause then the argument of that clause becomes the anchor of the step.

### The it() function

Another magical shortcut is offered by the `it()` function. The it function can be used to reference the anchor of the parent step. This allows for a more concise scenario description.
