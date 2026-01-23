# Writing specs

## The specification files are written in Python and rendered to Markdown

The specification files (typically placed in the extra/spec_src) are written in Python since this allows us to use them programatically to create comprehensive project documentation. Using the sunya tool, these Python spec_srec files are rendered to Markdown (and typically placed in the doc/spec directory) before they are used during implementation.

## The module specifications

The module specification files define various data-structures. A scenario spec may also (implicitly) define a code-unit in the module spec. E.g. the scenario spec may refer to Users.Actions.DeleteUser, which means that the Users module has a DeleteUser action function.
It commonly happens that in such cases the Users module doesn't explicitly declare an Actions section. This is okay, as sunya will automatically add this section later when it renders the spec_src into the Markdown specs.

### The external.py module

This module is special case. It doesn't exist in the spec_src as it is only used as a "virtual" namespace for any external actors.

### The settings section

The settings section is special because its contents should be used not in the module directly but in the global settings file that exists at the root of the Python application package that is being specced.

## The scenarios

The scenarios describe sequence diagrams that reference the module spec. The blogs/backend/scenarios/ms1_a_user_creates_a_blog/scenario.py gives an example of a backend scenario file for the first milestone in the example roadmap.

Scenarios can declare goals and steps. Steps are small actions that contribute to completing the workflow in a milestone. A goal describes a group of steps that work towards the same (intermediate) result. Steps are usually nested within a goal.

The scenario source code will use the actions namespace (`a`) to define the relation between the actors that participate in a step. The action namespace supports the following actions: `calls(*args, **kwargs)`, `creates(arg)`, `returns(arg)` and `rel(it().does_something_with(r.some_other_thing))`. The latter form is used for generic action descriptions.

Note that the scenario may refer to a `form` argument. This typically means that the actors (e.g. the target `book` instance) are passed as separate arguments, but the action values (e.g. the new book title and book status) are passed in a single object.
