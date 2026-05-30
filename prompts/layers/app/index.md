# General instructions for writing applications

# Using specifications

## 1. Writing Specifications

If you're writing specifications:

- Start with [./writing_specs/instructions-for-writing-specs.md](./writing_specs/instructions-for-writing-specs.md)
- See examples in [examples/bookie/extra/spec_src/scenarios/](examples/bookie/extra/spec_src/scenarios/)

**[./writing_specs/instructions-for-writing-specs.md](./writing_specs/instructions-for-writing-specs.md)**

- How to write scenario specs
- Implicit code-unit declarations in scenarios
- Scenario syntax and DSL (goals, steps, markdown sections)
- The `sunya` package and special modules

## 2. Mapping Specs to Implementation

If you're implementing from specifications:

- Start with [./using_specs/instructions-for-mapping-specs-to-implementation.md](./using_specs/instructions-for-mapping-specs-to-implementation.md)
- Then read [general code generation instructions](./general_code_generation_instructions/) — rules for following project instructions and using example code as templates

**[./using_specs/instructions-for-mapping-specs-to-implementation.md](./using_specs/instructions-for-mapping-specs-to-implementation.md)**

- Module specs → feature packages
- Section naming conventions (PascalCase → snake_case)
- File structure patterns
- Settings consolidation
- Validation approach

## Notes

- The `External` module is virtual and only used for external actors in scenarios
- All code-units (actions, models, rules, etc.) are implicitly declared in scenario specs
- The `sunya` package renders specs to Markdown but this is optional for implementation
