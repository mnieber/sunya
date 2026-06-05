# Target: local_env

This target describes how to set up and manage a **local development environment** for a stack containing multiple services and applications.

## Scope

This target covers:
- Docker Compose configuration for local development
- Just commands (Justfile) for managing the local stack
- Environment file structure and management
- Service orchestration and dependencies
- Local infrastructure services (databases, LocalStack, etc.)

This target does **not** cover:
- Individual service/application code (see targets/django_app, targets/react_app, etc.)
- CI/CD environments (see targets/ci_env when available)
- Production deployments

## What is a local_env stack?

A local_env stack is a complete local development environment where:
- All services run in Docker containers via Docker Compose
- Services can communicate with each other via Docker networking
- Developers use Just commands to manage the stack (start, stop, run tests, etc.)
- Environment variables are managed through .env files
- Local infrastructure (databases, message queues, etc.) runs alongside application services

## Layers used

This target composes the following layers:

- **layers/docker** - Docker Compose patterns, Dockerfile patterns, service orchestration
- **layers/just** - Justfile commands for managing the local development workflow

## Example application

The `examples/blogs/` directory demonstrates a complete local development stack containing:
- Backend service (Django)
- Frontend service (React)
- PostgreSQL database
- Docker Compose configuration
- Just commands for common operations
- Environment file structure

## File structure overview

```
<stack>/
├── env/
│   └── local/
│       ├── docker/
│       │   ├── docker-compose.yml
│       │   └── env_files/
│       │       ├── <service>.env
│       │       └── ...
│       └── secrets.env
├── src/
│   ├── services/
│   │   ├── <service_name>/
│   │   │   ├── Dockerfile
│   │   │   └── ...
│   │   └── ...
│   └── libs/
│       └── <lib_name>/
│           └── ...
├── Justfile
└── dodo.py
```

## Getting started

For detailed instructions on:
- Setting up Docker Compose configuration → see `layers/docker/index.md`
- Creating Just commands → see `layers/just/index.md`
- Adding specific services/infrastructure → see skills in `layers/docker/skills/`
