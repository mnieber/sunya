# Instructions for working on a stack

A stack contains various services and applications. The code generation instructions for each contained service or application are given in the respective target directory for that service or application (e.g. targets/django_app). In the current targets/stack directory, we will describe how to generate the stack code that will allow us to manage these services and applications.

## Overview

The development process follows two main phases:

1. **Writing Specifications** - Define scenario specs that describe what the application should do
2. **Create an implementation plan based on skills** - Based on the specifications, create a high-level implementation plan that refers to the skills needed.
3. **Implementation** - Map specifications to actual Python code following the consistent patterns described in the skills.

## Quick Start

Consult app_layer/index.md for instructions on:

- writing specifications
- implementing specifications
- general code generation guidelines

## Reference app

The [examples/bookie/](examples/bookie/) directory contains a complete example application showing:

- Spec files: `extra/spec_src/scenarios/`
- Implementation: `src/bookie/`
- How specs map to actual code
