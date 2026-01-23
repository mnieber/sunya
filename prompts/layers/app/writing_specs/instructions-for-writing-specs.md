# Writing specs

When writing an scenario spec file, please follow the example in `spec_src/scenarios/ms1_a_user_creates_a_book/scenario.py`. When wring a module spec file, follow the examples in `spec_src/modules`.

## Scenarios may declare that certain code-units exist in a module.

A scenario spec may implicitly define a code-unit in the module spec. E.g. the bookie scenario spec contains a reference to `m.Books.Actions.CreateBook` which implies that the books module has an Actions section with a CreateBook action.

## Specs import from the sunya package

The sunya package can be used to render the spec_src to Markdown files. However, for our purposes, we can leave this step out of consideration.

### The external.py module

This module is special case. It doesn't exist in the spec_src as it is only used as a "virtual" namespace for any external actors. This is why there is no `modules/external.py` in the bookie module specs although the bookie scenario spec mentions `m.External.Actors.User`.

## The scenarios

The scenarios describe sequence diagrams that reference the module spec.

Scenarios can declare goals and steps. Steps are small actions that contribute to completing the workflow in a milestone. A goal describes a group of steps that work towards the same (intermediate) result. Steps are usually nested within a goal.

The scenario source code will use the actions namespace (`a`) to define the relation between the actors that participate in a step. The action namespace supports the following actions: `calls(*args, **kwargs)`, `creates(arg)`, `returns(arg)` and `rel(it().does_something_with(r.some_other_thing))`. The latter form is used for generic action descriptions.
