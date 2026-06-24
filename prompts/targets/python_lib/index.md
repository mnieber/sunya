# Spec-Driven Development for Python Libraries

This directory contains instructions for a spec-driven software development process where specifications are written first, then mapped to implementation.

## Overview

The development process follows two main phases:

1. **Writing Specifications** - Define scenario specs that describe what the application should do
2. **Create an implementation plan based on skills** - Before writing the plan, read [python_lib/index.md](./python_lib_layer/index.md) to identify which skills apply to the code units you need to generate. Then create a high-level implementation plan that refers to those skills.
3. **Implementation** - Map specifications to actual Python code following the consistent patterns described in the skills.

## Quick Start

Consult ./app_layer/index.md for instructions on:

- writing specifications
- implementing specifications
- general code generation guidelines

Consult ./python_lib_layer/index.md for instructions on:

- Using specific python_lib skills, such as py-write-action.

## Examples

The [examples/bookie/](./examples/bookie/) directory contains a complete example application showing:

- Spec files: `extra/spec_src/scenarios/`
- Implementation: `src/bookie/`
- How specs map to actual code

## Key Principles

- **One file per code unit** - Each model, action, rule, or util gets its own file
- **Snake_case file names** - Convert PascalCase spec names to snake_case
- **Forms co-location** - Forms are defined in the action files that use them
- **Settings consolidation** - All module settings go to root settings.py
- **Explicit is better** - When in doubt, ask for spec clarification rather than guessing
