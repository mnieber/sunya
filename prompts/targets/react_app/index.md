# Spec-Driven Development for React Apps

This directory contains instructions for a spec-driven software development process where specifications are written first, then mapped to a React/TypeScript frontend application.

## Overview

The development process follows two main phases:

1. **Writing Specifications** - Define scenario specs that describe what the application should do
2. **Implementing from Specs** - Map specifications to actual React/TypeScript code following consistent patterns

## Quick Start

### If you're writing specifications:

- Start with [writing_specs/instructions-for-writing-specs.md](writing_specs/instructions-for-writing-specs.md)
- See examples in [examples/blogs_fe/extra/spec_src/scenarios/](examples/blogs_fe/extra/spec_src/scenarios/)

### If you're implementing from specifications:

- Start with [using_specs/instructions-for-mapping--specs-to-implementation.md](using_specs/instructions-for-mapping--specs-to-implementation.md)
- Understand the React-specific spec sections in [using_specs/structure-of-a-react-app-module-spec.md](using_specs/structure-of-a-react-app-module-spec.md)
- Then refer to the detailed implementation guides below

## Documentation Structure

### 1. General Code Generation Instructions

- **[general_code_generation_instructions/general code generation instructions.md](general_code_generation_instructions/general%20code%20generation%20instructions.md)**
  - Rules for following project instructions
  - Using example code as templates

- **[general_code_generation_instructions/project_structure.md](general_code_generation_instructions/project_structure.md)**
  - Three-step development process: roadmap, spec_src, application code

### 2. Writing Specifications

**[writing_specs/instructions-for-writing-specs.md](writing_specs/instructions-for-writing-specs.md)**

- How to write scenario specs
- Implicit code-unit declarations in scenarios
- Scenario syntax and DSL (goals, steps, markdown sections)
- The special `External` virtual namespace

### 3. React App Spec Sections

**[using_specs/structure-of-a-react-app-module-spec.md](using_specs/structure-of-a-react-app-module-spec.md)**

- React-specific spec sections declared implicitly in scenarios: Types, Mutations, Queries, States, Routes, StateProviders, Views, Effects, Components
- Facet types available on State containers (data, selection, highlight, addition, deletion, edit, etc.)

### 4. Mapping Specs to Implementation

**[using_specs/instructions-for-mapping--specs-to-implementation.md](using_specs/instructions-for-mapping--specs-to-implementation.md)**

- Module namespaces to feature package directories
- File structure patterns
- One file per code unit (camelCase filenames matching spec names)

### 5. React Code Implementation Guides

#### API layer

- **[instructions for writing model type files.md](./writing_code/instructions%20for%20writing%20model%20type%20files.md)**
  - TypeScript types with `T` suffix and `create` factory functions
  - `EntityT` mixin, resource-state initialization

- **[instructions for writing model schema files.md](./writing_code/instructions%20for%20writing%20model%20schema%20files.md)**
  - Zod schema definitions for API response validation

- **[instructions for writing query hooks.md](./writing_code/instructions%20for%20writing%20query%20hooks.md)**
  - Query hooks using `useObservableQuery`, camelCase conversion, optional `enabled` flag

- **[instructions for writing mutation hooks.md](./writing_code/instructions%20for%20writing%20mutation%20hooks.md)**
  - Mutation hooks using `useObservableMutation`, camelCase-to-snake-case post conversion

- **[instructions for writing msw handlers.md](./writing_code/instructions%20for%20writing%20msw%20handlers.md)**
  - MSW mock handlers for queries (used in Storybook and tests)

#### State layer

- **[instructions for writing State ts files.md](./writing_code/instructions%20for%20writing%20State%20ts%20files.md)**
  - State classes with containers, facets, props, and `registerCtr`
  - `actionsCtr` for simple direct actions that don't warrant a facet

- **[instructions for writing a useState ts file.md](./writing_code/instructions%20for%20writing%20a%20useState%20ts%20file.md)**
  - `useState` hooks, resource-state tracking, `graftResourceStatesFromMemo`, `trackPromise`

- **[instructions for writing registerCtr files.md](./writing_code/instructions%20for%20writing%20registerCtr%20files.md)**
  - Wiring facet outputs to inputs, `setCallbacks` for side-effects on facet operations

- **[instructions for writing a routes ts file.md](./writing_code/instructions%20for%20writing%20a%20routes%20ts%20file.md)**
  - `Nav` and `DefaultNav` classes delegating to the global `navHandler`

#### Component layer

- **[instructions for writing a component file.md](./writing_code/instructions%20for%20writing%20a%20component%20file.md)**
  - General React component patterns: props not unpacked, `L` layout object, intrinsic vs. ad-hoc styles, scss files

- **[instructions for writing a StateProvider tsx file.md](./writing_code/instructions%20for%20writing%20a%20StateProvider%20tsx%20file.md)**
  - One StateProvider per State; cache object, `updateSources`, `createGetProps`, MobX + React Context

- **[instructions for writing a FormView tsx file.md](./writing_code/instructions%20for%20writing%20a%20FormView%20tsx%20file.md)**
  - `withContextProps` HOC, `FormFieldLabel` buttons, `Field` context component

- **[instructions for writing a form ts file.md](./writing_code/instructions%20for%20writing%20a%20form%20ts%20file.md)**
  - `getInitialValues` to declare fields and initial values, `getInitialErrors` for external errors

- **[instructions for writing a ListView tsx file.md](./writing_code/instructions%20for%20writing%20a%20ListView%20tsx%20file.md)**
  - ListView and ListViewItem component patterns

- **[instructions for writing a SelectEffect tsx file.md](./writing_code/instructions%20for%20writing%20a%20SelectEffect%20tsx%20file.md)**
  - URL-driven resource selection via the selection facet; `UrlEffectView` sync warning

- **[instructions for writing a CreateEffect tsx file.md](./writing_code/instructions%20for%20writing%20a%20CreateEffect%20tsx%20file.md)**
  - URL-driven transient-instance creation via `addition.add()`

- **[instructions for writing a trimmed component.md](./writing_code/instructions%20for%20writing%20a%20trimmed%20component.md)**
  - `trim.ts` (trim type + style object) and `trims.ts` (pre-made trim variants)

- **[instructions for writing a Menu tsx file.md](./writing_code/instructions%20for%20writing%20a%20Menu%20tsx%20file.md)**
  - Menu component pattern

- **[instructions for writing App tsx files.md](./writing_code/instructions%20for%20writing%20App%20tsx%20files.md)**
  - Provider placement strategy, Switches for route grouping

- **[instructions for writing a storybook tsx file.md](./writing_code/instructions%20for%20writing%20a%20storybook%20tsx%20file.md)**
  - One story per standalone View or reusable Component; MSW mocks for query data

- **[instructions for writing a mock component file.md](./writing_code/instructions%20for%20writing%20a%20mock%20component%20file.md)**
  - Mock components: name prefix `Mock`, TailwindCSS, single-file, renderable in artifact viewer

## Examples

The [examples/](examples/) directory contains one complete example application:

- **[examples/blogs_fe/](examples/blogs_fe/)** - A blogs frontend showing all React patterns (types, mutations, queries, state, state-providers, views, effects, routes, forms, storybook, msw mocks)

## Spec Section to Implementation Mapping

| Spec Section                    | Implementation Location                              | Documented In                                      |
| ------------------------------- | ---------------------------------------------------- | -------------------------------------------------- |
| Module.Types.X                  | api/types/XT.ts + XSchema.ts                         | instructions for writing model type/schema files   |
| Module.Mutations.X              | api/mutations/useX.ts                                | instructions for writing mutation hooks            |
| Module.Queries.X                | api/queries/useX.ts                                  | instructions for writing query hooks               |
| Module.States.XState            | module/XState/XState.ts + XData.ts + registerXCtr.ts | instructions for writing State ts files            |
| Module.Routes.X                 | module/routes.ts (Nav + DefaultNav)                  | instructions for writing a routes ts file          |
| Module.StateProviders.XProvider | module/components/XStateProvider.tsx                 | instructions for writing a StateProvider tsx file  |
| Module.Views.X                  | module/components/X.tsx (+ form.ts if form-based)    | instructions for writing a FormView/ListView file  |
| Module.Effects.X                | module/components/XEffect.tsx                        | instructions for writing SelectEffect/CreateEffect |
| Module.Components.X             | module/components/X/ (trim.ts, trims.ts, X.tsx)      | instructions for writing a trimmed component       |

## Development Workflow

1. **Define specs** - Write scenario specs in `extra/spec_src/scenarios/`
2. **Review specs** - Ensure clarity; ask for clarification if needed
3. **Implement** - Map specs to code following the implementation guides
4. **Validate** - Specs owner validates implementation matches intent

## Key Principles

- **camelCase file names** - File and directory names match the spec name in camelCase (e.g. `BlogPostsState/`, `useCreateBlog.ts`)
- **One file per code unit** - Each mutation hook, query hook, State, StateProvider, or component gets its own file
- **Props not unpacked** - Component props are accessed as `props.foo`, not destructured
- **MobX + React Context** - State is MobX-observable; Contexts pass it to consuming components
- **Types in api module** - TypeScript types often live in the `api/types/` directory since they cut across feature modules
- **Follow the examples** - The blogs_fe example serves as the primary reference template
- **Explicit is better** - When in doubt, ask for spec clarification rather than guessing
