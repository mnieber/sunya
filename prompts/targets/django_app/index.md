# Spec-Driven Development for Django Apps

This directory contains instructions for a spec-driven software development process where specifications are written first, then mapped to a Django application.

## Overview

The development process follows two main phases:

1. **Writing Specifications** - Define module specs and scenario specs that describe what the application should do
2. **Implementing from Specs** - Map specifications to actual Django and Python code following consistent patterns

## Quick Start

### If you're writing specifications:

- Start with [writing_specs/instructions-for-writing-specs.md](writing_specs/instructions-for-writing-specs.md)
- See examples in [examples/bookie/extra/spec_src/](examples/bookie/extra/spec_src/) and [examples/blogs_be/extra/spec_src/](examples/blogs_be/extra/spec_src/)

### If you're implementing from specifications:

- Start with [using_specs/instructions-for-mapping--specs-to-implementation.md](using_specs/instructions-for-mapping--specs-to-implementation.md)
- Understand the Django-specific spec sections in [using_django_app_specs/sections-of-a-django-app-module-spec.md](using_django_app_specs/sections-of-a-django-app-module-spec.md)
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

- How to write module specs and scenario specs
- Implicit vs. explicit code-unit declarations
- Scenario syntax and DSL
- The special `external.py` virtual namespace

### 3. Understanding Django App Specs

**[using_django_app_specs/sections-of-a-django-app-module-spec.md](using_django_app_specs/sections-of-a-django-app-module-spec.md)**

- Django-specific module spec sections: Django models, ApiViews, DomainEvents

### 4. Mapping Specs to Implementation

**[using_specs/instructions-for-mapping--specs-to-implementation.md](using_specs/instructions-for-mapping--specs-to-implementation.md)**

- Module specs to feature packages
- Section naming conventions
- File structure patterns

### 5. Django Code Implementation Guides

Located in [writing_django_code/](writing_django_code/):

- **[instructions-for-writing-models.md](writing_django_code/instructions-for-writing-models.md)**

  - Django model patterns (e.g. SingleLineTextField for short strings)

- **[instructions-for-writing-api-views.md](writing_django_code/instructions-for-writing-api-views.md)**

  - REST API view structure, permissions, and data specs

- **[instructions-for-writing-serializers.md](writing_django_code/instructions-for-writing-serializers.md)**

  - Django REST framework serializer patterns

- **[instructions-for-writing-urls.md](writing_django_code/instructions-for-writing-urls.md)**

  - URL configuration patterns

- **[instructions-for-writing-permissions.md](writing_django_code/instructions-for-writing-permissions.md)**

  - Permission class patterns

- **[instructions-for-writing-admin.md](writing_django_code/instructions-for-writing-admin.md)**

  - Django admin configuration

- **[instructions-for-writing-factories.md](writing_django_code/instructions-for-writing-factories.md)**

  - Factory classes for testing

- **[instructions-for-writing-schemas.md](writing_django_code/instructions-for-writing-schemas.md)**

  - Pydantic schema classes for JSON blob structures

- **[instructions-for-writing-shortcuts.md](writing_django_code/instructions-for-writing-shortcuts.md)**

  - Shortcut function patterns

- **[instructions-for-writing-tests.md](writing_django_code/instructions-for-writing-tests.md)**

  - Tests for actions, API views, and permissions (including checks_permission usage)

### 6. Python Package Code Implementation Guides

Located in [writing_python_package_code/](writing_python_package_code/):

- **[instructions-for-writing-actions.md](writing_python_package_code/instructions-for-writing-actions.md)**

  - Action functions and their file structure
  - Forms co-location with actions
  - Exception handling patterns

- **[instructions-for-writing-models.md](writing_python_package_code/instructions-for-writing-models.md)**

  - Data model class structure (dataclass patterns)

- **[instructions-for-writing-rule-files.md](writing_python_package_code/instructions-for-writing-rule-files.md)**

  - Pure business logic functions (opinionated, don't modify state)
  - Rule vs. action distinction

- **[instructions-for-writing-utils-files.md](writing_python_package_code/instructions-for-writing-utils-files.md)**

  - Utility function patterns (unopinionated helpers)

- **[instructions-for-writing-settings.md](writing_python_package_code/instructions-for-writing-settings.md)**

  - Centralized settings.py structure
  - Environment variable handling

- **[instructions-for-writing-python-files.md](writing_python_package_code/instructions-for-writing-python-files.md)**

  - General Python code conventions (no docstrings, inline comments, logging)

- **[instructions-for-writing-schemas.md](writing_python_package_code/instructions-for-writing-schemas.md)**

  - Pydantic schema definitions for JSON blobs

- **[instructions-for-writing-enums-files.md](writing_python_package_code/instructions-for-writing-enums-files.md)**

  - Enum class definitions

- **[instructions-for-writing-entrypoints.md](writing_python_package_code/instructions-for-writing-entrypoints.md)**

  - Application entry points with argparse

## Examples

The [examples/](examples/) directory contains two complete example applications:

- **[examples/blogs_be/](examples/blogs_be/)** - A blogs backend showing Django-specific patterns (models, API views, serializers, admin, urls, permissions, factories, tests)
- **[examples/bookie/](examples/bookie/)** - A bookie application showing Python package patterns (actions, rules, utils, settings, enums, entrypoints)

## Spec Section to Implementation Mapping

### Django Code

| Spec Section              | Implementation Location                    | Documented In                              |
| ------------------------- | ------------------------------------------ | ------------------------------------------ |
| Module.DjangoModels.X     | module/models.py (X class)                 | writing_django_code/instructions-for-writing-models.md |
| Module.ApiViews.X         | module/api_views.py                        | writing_django_code/instructions-for-writing-api-views.md |
| Module.Serializers        | module/serializers.py                      | writing_django_code/instructions-for-writing-serializers.md |
| Module.Urls               | module/urls.py                             | writing_django_code/instructions-for-writing-urls.md |
| Module.Permissions        | module/permissions.py                      | writing_django_code/instructions-for-writing-permissions.md |
| Module.Admin              | module/admin.py                            | writing_django_code/instructions-for-writing-admin.md |
| Module.Factories          | module/factories.py                        | writing_django_code/instructions-for-writing-factories.md |

### Python Package Code

| Spec Section       | Implementation Location               | Documented In                                              |
| ------------------ | ------------------------------------- | ---------------------------------------------------------- |
| Module.Models.X    | module/models/x.py (X class)         | writing_python_package_code/instructions-for-writing-models.md |
| Module.Actions.X   | module/actions/x.py (x function)     | writing_python_package_code/instructions-for-writing-actions.md |
| Module.Forms.XForm | Co-located in action file (dataclass) | writing_python_package_code/instructions-for-writing-actions.md |
| Module.Rules.X     | module/rules/x.py (x function)       | writing_python_package_code/instructions-for-writing-rule-files.md |
| Module.Utils.X     | module/utils/x.py (x function)       | writing_python_package_code/instructions-for-writing-utils-files.md |
| Module.Settings.X  | settings.py at app root (constant)   | writing_python_package_code/instructions-for-writing-settings.md |
| Module.Enums.X     | module/enums.py (X class)            | writing_python_package_code/instructions-for-writing-enums-files.md |

## Development Workflow

1. **Define specs** - Write module and scenario specs in `extra/spec_src/`
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
