# Spec-Driven Development for Python Libraries

This directory contains instructions for a spec-driven software development process where specifications are written first, then mapped to implementation.

## Overview

The development process follows two main phases:

1. **Writing Specifications** - Define scenario specs that describe what the application should do
2. **Create an implementation plan based on skills** - Based on the specifications, create a high-level implementation plan that refers to the skills needed. Skills for building a Python library are contained in `python_lib_skills/` and listed in this file.
3. **Implementation** - Map specifications to actual Python code following the consistent patterns described in the skills.

## Quick Start

### If you're writing specifications:

- Start with [app_layer/writing_specs/instructions-for-writing-specs.md](app_layer/writing_specs/instructions-for-writing-specs.md)
- See examples in [examples/bookie/extra/spec_src/scenarios/](examples/bookie/extra/spec_src/scenarios/)

### If you're implementing from specifications:

- Start with [app_layer/using_specs/instructions-for-mapping-specs-to-implementation.md](app_layer/using_specs/instructions-for-mapping-specs-to-implementation.md)
- Then read [general code generation instructions](app_layer/general_code_generation_instructions/) — rules for following project instructions and using example code as templates
- Then follow the high-level plan and consult [python_lib_skills/index.md](python_lib_skills/index.md) for the available skills.

## Documentation Structure

### 1. Writing Specifications

**[app_layer/writing_specs/instructions-for-writing-specs.md](app_layer/writing_specs/instructions-for-writing-specs.md)**

- How to write scenario specs
- Implicit code-unit declarations in scenarios
- Scenario syntax and DSL (goals, steps, markdown sections)
- The `sunya` package and special modules

### 2. Mapping Specs to Implementation

**[app_layer/using_specs/instructions-for-mapping-specs-to-implementation.md](app_layer/using_specs/instructions-for-mapping-specs-to-implementation.md)**

- Module specs → feature packages
- Section naming conventions (PascalCase → snake_case)
- File structure patterns
- Settings consolidation
- Validation approach

### 3. Skills

See **[python_lib_skills/index.md](python_lib_skills/index.md)** for the full list of available skills.

## Examples

The [examples/bookie/](examples/bookie/) directory contains a complete example application showing:

- Spec files: `extra/spec_src/scenarios/`
- Implementation: `src/bookie/`
- How specs map to actual code

## Spec Section to Implementation Mapping

| Spec Section       | Implementation Location               | Skill                |
| ------------------ | ------------------------------------- | -------------------- |
| Module.Models.X    | module/models/x.py (X class)          | py-write-model.md    |
| Module.Actions.X   | module/actions/x.py (x function)      | py-write-action.md   |
| Module.Forms.XForm | Co-located in action file (dataclass) | py-write-action.md   |
| Module.Rules.X     | module/rules/x.py (x function)        | py-write-rule.md     |
| Module.Utils.X     | module/utils/x.py (x function)        | py-write-util.md     |
| Module.Settings.X  | settings.py at app root (constant)    | py-write-settings.md |
| Module.Enums.X     | module/enums.py (X class)             | py-write-enums.md    |

## Development Workflow

1. **Define specs** - Write scenario specs in `extra/spec_src/scenarios/`
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
- All code-units (actions, models, rules, etc.) are implicitly declared in scenario specs
- The `sunya` package renders specs to Markdown but this is optional for implementation
