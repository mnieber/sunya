# Spec-Driven Development for Django Apps

This directory contains instructions for a spec-driven software development process where specifications are written first, then mapped to a Django application.

## Overview

The development process follows two main phases:

1. **Writing Specifications** - Define scenario specs that describe what the application should do
2. **Implementing from Specs** - Map specifications to actual Django and Python code following consistent patterns

## Quick Start

### If you're writing specifications:

- Start with [writing_specs/instructions-for-writing-specs.md](writing_specs/instructions-for-writing-specs.md)
- See examples in [examples/bookie/extra/spec_src/scenarios/](examples/bookie/extra/spec_src/scenarios/) and [examples/blogs_be/extra/spec_src/scenarios/](examples/blogs_be/extra/spec_src/scenarios/)

### If you're implementing from specifications:

- Start with [using_specs/instructions-for-mapping-specs-to-implementation.md](using_specs/instructions-for-mapping-specs-to-implementation.md)
- Understand the Django-specific spec sections in [using_django_app_specs/sections-of-a-django-app-module-spec.md](using_django_app_specs/sections-of-a-django-app-module-spec.md)
- Then read [general code generation instructions](general_code_generation_instructions/) — rules for following project instructions and using example code as templates
- Then follow the high-level plan and consult [django_app_layer/index.md](django_app_layer/index.md) for Django skills and [python_lib_layer/index.md](python_lib_layer/index.md) for Python package skills

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

### 3. Django App Spec Sections

**[using_django_app_specs/sections-of-a-django-app-module-spec.md](using_django_app_specs/sections-of-a-django-app-module-spec.md)**

- Django-specific spec sections declared implicitly in scenarios: Django models, ApiViews, DomainEvents

### 4. Mapping Specs to Implementation

**[using_specs/instructions-for-mapping-specs-to-implementation.md](using_specs/instructions-for-mapping-specs-to-implementation.md)**

- Module specs to feature packages
- Section naming conventions
- File structure patterns

### 5. Django Skills

See **[django_app_layer/index.md](django_app_layer/index.md)** for the full list of available Django skills.

### 6. Python Package Skills

See **[python_lib_layer/index.md](python_lib_layer/index.md)** for the full list of available Python package skills.

## Examples

The [examples/](examples/) directory contains two complete example applications:

- **[examples/blogs_be/](examples/blogs_be/)** - A blogs backend showing Django-specific patterns (models, API views, serializers, admin, urls, permissions, factories, tests)
- **[examples/bookie/](examples/bookie/)** - A bookie application showing Python package patterns (actions, rules, utils, settings, enums, entrypoints)

## Spec Section to Implementation Mapping

### Django Code

| Spec Section          | Implementation Location    | Skill                                        |
| --------------------- | -------------------------- | -------------------------------------------- |
| Module.DjangoModels.X | module/models.py (X class) | django_app_layer: dj-write-model             |
| Module.ApiViews.X     | module/api_views.py        | django_app_layer: dj-write-api-view          |
| Module.Serializers    | module/serializers.py      | django_app_layer: dj-write-serializer        |
| Module.Urls           | module/urls.py             | django_app_layer: dj-write-urls              |
| Module.Permissions    | module/permissions.py      | django_app_layer: dj-write-permissions       |
| Module.Admin          | module/admin.py            | django_app_layer: dj-write-admin             |
| Module.Factories      | module/factories.py        | django_app_layer: dj-write-factories         |

### Python Package Code

| Spec Section       | Implementation Location               | Skill                              |
| ------------------ | ------------------------------------- | ---------------------------------- |
| Module.Models.X    | module/models/x.py (X class)          | python_lib_layer: py-write-model   |
| Module.Actions.X   | module/actions/x.py (x function)      | python_lib_layer: py-write-action  |
| Module.Forms.XForm | Co-located in action file (dataclass) | python_lib_layer: py-write-action  |
| Module.Rules.X     | module/rules/x.py (x function)        | python_lib_layer: py-write-rule    |
| Module.Utils.X     | module/utils/x.py (x function)        | python_lib_layer: py-write-util    |
| Module.Settings.X  | settings.py at app root (constant)    | python_lib_layer: py-write-settings|
| Module.Enums.X     | module/enums.py (X class)             | python_lib_layer: py-write-enums   |

## Development Workflow

1. **Define specs** - Write scenario specs in `extra/spec_src/scenarios/`
2. **Review specs** - Ensure clarity; ask for clarification if needed
3. **Implement** - Map specs to code following the implementation guides
4. **Validate** - Specs owner validates implementation matches intent

## Key Principles

- **One file per code unit** - Each action, rule, or util gets its own file
- **Snake_case file names** - Convert PascalCase spec names to snake_case
- **Forms co-location** - Forms are defined in the action files that use them
- **Settings consolidation** - All module settings go to root settings.py
- **Follow the examples** - The blogs_be and bookie examples serve as reference templates
- **Explicit is better** - When in doubt, ask for spec clarification rather than guessing
