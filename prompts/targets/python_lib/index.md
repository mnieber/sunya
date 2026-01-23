# Spec-Driven Development for Python Libraries

This directory contains instructions for a spec-driven software development process where specifications are written first, then mapped to implementation.

## Overview

The development process follows two main phases:

1. **Writing Specifications** - Define module specs and scenario specs that describe what the application should do
2. **Implementing from Specs** - Map specifications to actual Python code following consistent patterns

## Quick Start

### If you're writing specifications:

- Start with [writing_specs/instructions-for-writing-specs.md](writing_specs/instructions-for-writing-specs.md)
- See examples in [examples/bookie/extra/spec_src/](examples/bookie/extra/spec_src/)

### If you're implementing from specifications:

- Start with [using_specs/instructions-for-mapping--specs-to-implementation.md](using_specs/instructions-for-mapping--specs-to-implementation.md)
- Then refer to the detailed implementation guides below

## Documentation Structure

### 1. Writing Specifications

**[writing_specs/instructions-for-writing-specs.md](writing_specs/instructions-for-writing-specs.md)**

- How to write module specs and scenario specs
- Implicit vs. explicit code-unit declarations
- Scenario syntax and DSL (sequence diagrams, goals, steps)
- The `sunya` package and special modules

### 2. Mapping Specs to Implementation

**[using_specs/instructions-for-mapping--specs-to-implementation.md](using_specs/instructions-for-mapping--specs-to-implementation.md)**

- Module specs → feature packages
- Section naming conventions (PascalCase → snake_case)
- File structure patterns
- Settings consolidation
- Validation approach

### 3. Detailed Implementation Guides

Located in [writing_python_package_code/](writing_python_package_code/):

- **[instructions-for-writing-actions.md](writing_python_package_code/instructions-for-writing-actions.md)**

  - Action functions and their file structure
  - Forms co-location with actions
  - Exception handling patterns
  - Helper function conventions

- **[instructions-for-writing-models.md](writing_python_package_code/instructions-for-writing-models.md)**

  - Model class structure
  - Data class patterns

- **[instructions-for-writing-rule-files.md](writing_python_package_code/instructions-for-writing-rule-files.md)**

  - Pure functions that don't modify state
  - Rule vs. action distinction

- **[instructions-for-writing-utils-files.md](writing_python_package_code/instructions-for-writing-utils-files.md)**

  - Utility function patterns
  - Helper code organization

- **[instructions-for-writing-settings.md](writing_python_package_code/instructions-for-writing-settings.md)**

  - Centralized settings.py structure
  - Environment variable handling
  - Settings consolidation from module specs

- **[instructions-for-writing-python-files.md](writing_python_package_code/instructions-for-writing-python-files.md)**

  - General Python code conventions

- **[instructions-for-writing-schemas.md](writing_python_package_code/instructions-for-writing-schemas.md)**

  - Schema definitions

- **[instructions-for-writing-enums-files.md](writing_python_package_code/instructions-for-writing-enums-files.md)**

  - Enums

- **[instructions-for-writing-entrypoints.md](writing_python_package_code/instructions-for-writing-entrypoints.md)**
  - Application entry points

## Examples

The [examples/bookie/](examples/bookie/) directory contains a complete example application showing:

- Spec files: `extra/spec_src/modules/` and `extra/spec_src/scenarios/`
- Implementation: `src/bookie/`
- How specs map to actual code

## Spec Section to Implementation Mapping

| Spec Section       | Implementation Location               | Documented In                           |
| ------------------ | ------------------------------------- | --------------------------------------- |
| Module.Models.X    | module/models/x.py (X class)          | instructions-for-writing-models.md      |
| Module.Actions.X   | module/actions/x.py (x function)      | instructions-for-writing-actions.md     |
| Module.Forms.XForm | Co-located in action file (dataclass) | instructions-for-writing-actions.md     |
| Module.Rules.X     | module/rules/x.py (x function)        | instructions-for-writing-rule-files.md  |
| Module.Utils.X     | module/utils/x.py (x function)        | instructions-for-writing-utils-files.md |
| Module.Settings.X  | settings.py at app root (constant)    | instructions-for-writing-settings.md    |
| Module.Enums.X     | module/enums.py (X class)             | _(see bookie example)_                  |

## Development Workflow

1. **Define specs** - Write module and scenario specs in `extra/spec_src/`
2. **Review specs** - Ensure clarity; ask for clarification if needed
3. **Implement** - Map specs to code following the implementation guides
4. **Validate** - Specs owner validates implementation matches intent

## Key Principles

- **One file per code unit** - Each model, action, rule, or util gets its own file
- **Snake_case file names** - Convert PascalCase spec names to snake_case
- **Forms co-location** - Forms are defined in the action files that use them
- **Settings consolidation** - All module settings go to root settings.py
- **Explicit is better** - When in doubt, ask for spec clarification rather than guessing

## Notes

- The `External` module is virtual and only used for external actors in scenarios
- Actions can be implicitly defined in scenarios without being in module specs
- The `sunya` package renders specs to Markdown but this is optional for implementation
