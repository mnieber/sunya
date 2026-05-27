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

## Concerns and skills

When you are asked to generate code, or to plan for generating code, identify which of the below skills are needed and apply them.
Skills are in [react_app_skills/](react_app_skills/). Each skill is self-contained.

### Data model

Define a TypeScript type and its Zod validation schema for a new entity or value object.
→ [fe-add-model](react_app_skills/fe-add-model.md)

### API — queries and mutations

Write a `useQuery` hook and/or a `useMutation` hook to fetch or write data via the REST API.
→ [fe-add-api-hooks](react_app_skills/fe-add-api-hooks.md)

### API — MSW mock handlers

Add MSW handlers so the app and Storybook can run without a real backend. Also covers enabling MSW in `main.tsx`.
→ [fe-add-msw](react_app_skills/fe-add-msw.md)

### State layer

Provide MobX-based application state to the View components (containers, facets, `useXState` hook, `registerXCtr`, `XStateProvider`).
→ [fe-use-state-provider](react_app_skills/fe-use-state-provider.md)

### Routing

Define module routes (`XxxRoutes`, `XxxNav`, `DefaultXxxNavHandler`) and wire Switch components.
→ [fe-use-nav-handler](react_app_skills/fe-use-nav-handler.md)

### Form view

Write a form component (`XFormView.tsx`) and its companion `form.ts` (initial values, validation, submit, cancel).
→ [fe-create-formview](react_app_skills/fe-create-formview.md)

### List view

Write a `XListView` + `XListViewItem` with loading guard, keyboard selection, and highlight/selected styles.
→ [fe-add-list-view](react_app_skills/fe-add-list-view.md)

### Select effect

Write a `SelectXxxEffect` that reads a URL param and drives the selection facet (which is part of the state layer) when the URL changes.
→ [fe-add-select-effect](react_app_skills/fe-add-select-effect.md)

### Create effect

Write a `CreateXxxEffect` that instantiates a transient resource when the "create" route is entered. This effect is used in combination
with the addition facet (which is part of the state layer).

→ [fe-add-create-effect](react_app_skills/fe-add-create-effect.md)

### General component

Write a page, panel, or button component that reads MobX state and/or accepts layout props.
→ [fe-add-component](react_app_skills/fe-add-component.md)

### Trimmed component

Write a shared UI primitive (button, card, badge) with a structured `trim` styling interface.
→ [fe-add-trimmed-component](react_app_skills/fe-add-trimmed-component.md)

### App root

Compose providers, `AppBody`, and Switch components in `App.tsx`.
→ [fe-add-app-component](react_app_skills/fe-add-app-component.md)

### Storybook stories

Write isolated stories for standalone views and reusable components, backed by MSW handlers.
→ [fe-add-storybook](react_app_skills/fe-add-storybook.md)

---

## General code generation instructions

- [general code generation instructions](general_code_generation_instructions/general%20code%20generation%20instructions.md) — rules for following project instructions and using example code as templates
- [project structure](general_code_generation_instructions/project_structure.md) — codebase layout and development workflow

## Reference app

**[examples/blogs_fe/](examples/blogs_fe/)** — complete reference implementation; primary template for all patterns

## Key Principles

- **camelCase file names** - File and directory names match the spec name in camelCase (e.g. `BlogPostsState/`, `useCreateBlog.ts`)
- **One file per code unit** - Each mutation hook, query hook, State, StateProvider, or component gets its own file
- **Props not unpacked** - Component props are accessed as `props.foo`, not destructured
- **MobX + React Context** - State is MobX-observable; Contexts pass it to consuming components
- **Types in api module** - TypeScript types often live in the `api/types/` directory since they cut across feature modules
- **Follow the examples** - The blogs_fe example serves as the primary reference template
- **Explicit is better** - When in doubt, ask for spec clarification rather than guessing
