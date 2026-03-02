# Writing specs

When writing a scenario spec file, please follow the example in `extra/spec_src/scenarios/ms1_a_user_creates_a_book/scenario.py`.

## There are no explicit module spec files

Modules are defined implicitly through the scenario spec files. There is no `extra/spec_src/modules/` directory and no explicit module spec files. All code-unit declarations are made implicitly in the scenario files by referencing module paths such as `m.Books.Actions.CreateBook`.

## Scenarios may declare that certain code-units exist in a module.

A scenario spec implicitly defines code-units in a module. E.g. the bookie scenario spec contains a reference to `m.Books.Actions.CreateBook` (where `m` is the modules namespace) which implies that the books module has an Actions section with a CreateBook action.

## Specs import from the sunya package

The sunya package can be used to render the spec_src to Markdown files. However, for our purposes, we can leave this step out of consideration.

### The External module

The `External` module is a special virtual namespace used only for external actors in scenarios, such as `m.External.Actors.User`. There is no corresponding file for this module in the spec_src.

## The scenarios

Each scenario file contains:

1. A `run_scenario()` function that describes the scenario logic using the sunya Python DSL.
2. A `markdown_node` with a structured markdown section. This markdown section has a fixed format with **Steps** and **Diagram** subsections.

### The run_scenario function

The `run_scenario` function describes the scenario by:
- Assigning roles to module code-units using `r.<role> = m.<Module>.<Section>.<CodeUnit>`
- Describing goals and steps using `with goal()...` blocks and `the(...)` / `it()` step expressions

#### Goals

Every step must be nested inside a top-level goal. Goals are written as `with` blocks:

```python
with goal().create_a(r.result).using_the(r.foo):
    the(r.actor).does_something_with(r.foo)
```

#### Steps

Steps describe what each participant does. Every step starts with either:
- `the(r.actor).does_something()` — when naming a specific actor
- `it().does_something()` — as a shorthand referring back to the nearest preceding `the(...)` expression

Steps can be nested using `with`:

```python
with the(r.frontend).calls_the(r.action).with_the(r.form):
    it().validates(r.form)
    it().creates(r.result)
    it().returns(r.result)
```

### The markdown section

The markdown section uses this fixed structure:

```
A short description of the scenario.

### Steps

#### It does X

Step description.</br>

#### It does Y

Step description.</br>

### Diagram

\```mermaid
sequenceDiagram
    ...
\```
```

### The sunya DSL

Common patterns:
- `with goal().do_something(r.thing):` — a goal grouping steps
- `the(r.actor).calls(r.action).with_the(r.form)` — actor calls an action
- `it().creates(r.thing)` — creates something (shorthand for the nearest `the(...)`)
- `it().returns(r.thing)` — returns something
- `it().raises(r.error).if_something()` — raises an error conditionally
- `with the(r.actor).calls(r.action).with_the(r.form):` — a step with nested substeps
