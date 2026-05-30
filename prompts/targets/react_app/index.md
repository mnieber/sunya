# Spec-Driven Development for React Apps

This directory contains instructions for a spec-driven software development process where specifications are written first, then mapped to a React/TypeScript frontend application.

## Overview

The development process follows two main phases:

1. **Writing Specifications** - Define scenario specs that describe what the application should do.
2. **Create an implementation plan based on skills** - Based on the specifications, we'll create a high-level implementation plan that refers to the skills that are needed. E.g. the skills for building a react-app are contained in react_app/skills and are listed in react_app/index.md.
3. **Implementation** - Map specifications to actual React/TypeScript code following the consistent patterns described in the skills.

## Quick Start

### If you're writing specifications:

- Start with [writing_specs/instructions-for-writing-specs.md](writing_specs/instructions-for-writing-specs.md)
- See examples in [examples/blogs_fe/extra/spec_src/scenarios/](examples/blogs_fe/extra/spec_src/scenarios/)

### If you're implementing from specifications:

- Start with [using_specs/instructions-for-mapping-specs-to-implementation.md](using_specs/instructions-for-mapping-specs-to-implementation.md)
- Then read [general code generation instructions](general_code_generation_instructions/general%20code%20generation%20instructions.md) — rules for following project instructions and using example code as templates
- Then read [project structure](general_code_generation_instructions/project_structure.md) — codebase layout and development workflow
- Then follow the high-level plan and consult [react_app_layer/index.md](react_app_layer/index.md) for the available skills.

## Reference app

**[examples/blogs_fe/](examples/blogs_fe/)** — complete reference implementation; primary template for all patterns
