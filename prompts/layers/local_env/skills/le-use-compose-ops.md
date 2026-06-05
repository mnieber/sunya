# Skill: le-use-compose-ops

Applies when setting up Just commands to manage Docker Compose operations for the local development stack.

Primary reference: `examples/blogs/env/local/just/docker/`

---

## What this skill covers

This skill describes how to set up and use Just commands for Docker Compose operations:

- Setting up the justfile structure for compose operations
- Configuring ROOT_DIR, COMPOSE_DIR, and COMPOSE_PROJECT_NAME
- Using the standard compose operation commands

## What this skill does NOT cover

- **Service-specific Just commands** → see target-specific documentation (e.g., `targets/django_app`)
- **Compiling environment files** → covered briefly here, detailed in `layers/just/skills/just-compile-env-files.md`
- **Python-specific Just commands** → see `layers/just/skills/just-python-ops.md`

---

## Justfile structure

The stack uses a modular justfile structure:

```
<stack>/
├── justfile                           # Root justfile (delegates to env/local)
└── env/
    └── local/
        ├── justfile                   # Main local env justfile
        ├── .local.env                 # Developer-specific variables (gitignored)
        └── just/
            ├── docker/
            │   ├── index.just         # Docker operations coordinator
            │   ├── build.just         # Build commands
            │   ├── run.just           # Run commands (up, down, shell, run_cmd)
            │   ├── env-files.just     # Environment file compilation
            │   └── lib/               # Internal implementation helpers
            │       ├── _build.just
            │       ├── _build_base_images.just
            │       ├── _up.just
            │       ├── _down.just
            │       ├── _run_command.just
            │       └── _run_image.just
            └── python/
                └── index.just         # Python operations
```

---

## Step 1: Create the root justfile

Create `<stack>/justfile` that delegates to the local environment:

```makefile
import 'env/local/justfile'
```

**RULE:** The root justfile should be minimal and just import the environment-specific justfile.

Additional commands can be added here if they're environment-agnostic (e.g., a `pip-compile` command that delegates to `_pip_compile`).

---

## Step 2: Set up env/local/justfile

Create `<stack>/env/local/justfile` with the core configuration:

```makefile
import './just/docker/index.just'
import './just/python/index.just'

set dotenv-load := true
set dotenv-filename := 'env/local/.local.env'

# Determine root properties
export ROOT_DIR := canonicalize(source_directory() / "../..")
export HOST_IP := env_var_or_default("HOST_IP", `ip -4 addr show 2>/dev/null | grep -oP '(?<=inet\s)\d+(\.\d+){3}' | grep -v 127.0.0.1 | head -1 || echo ""`)
export PYTHON := `which python3 2>/dev/null || which python`

# Determine compose properties
export COMPOSE_DIR := source_directory() / "docker"
export COMPOSE_PROJECT_NAME := "blogs"
```

### Configuration variables

**ROOT_DIR:** Absolute path to the stack root directory
```makefile
export ROOT_DIR := canonicalize(source_directory() / "../..")
```
Uses `source_directory()` to get the justfile's location and goes up two levels to reach the stack root.

**COMPOSE_DIR:** Directory containing docker-compose files
```makefile
export COMPOSE_DIR := source_directory() / "docker"
```
Points to `env/local/docker/` where all compose files live.

**COMPOSE_PROJECT_NAME:** Docker Compose project name
```makefile
export COMPOSE_PROJECT_NAME := "blogs"
```
Replace `"blogs"` with your stack name. This determines the prefix for container names and networks.

**HOST_IP:** Host machine IP address (optional)
```makefile
export HOST_IP := env_var_or_default("HOST_IP", `ip -4 addr show 2>/dev/null | grep -oP '(?<=inet\s)\d+(\.\d+){3}' | grep -v 127.0.0.1 | head -1 || echo ""`)
```
Automatically detects the host IP for services that need to connect back to the host.

**PYTHON:** Python executable path
```makefile
export PYTHON := `which python3 2>/dev/null || which python`
```
Used by Python-related commands.

**RULE:** Always use `canonicalize()` for ROOT_DIR to ensure absolute paths.

**RULE:** The COMPOSE_PROJECT_NAME should match your stack name and be lowercase.

---

## Step 3: Create .local.env for developer settings

Create `<stack>/env/local/.local.env` for developer-specific variables (gitignored):

```bash
BLOGS_SHELL_COMMAND=fish
BLOGS_USE_DOCKERFILE_LOCAL=true
BLOGS_OS_CUSTOM_PACKAGES="nano curl fish"
```

**Common variables:**

- `<STACK>_SHELL_COMMAND`: Shell to use when running `just shell` (e.g., `bash`, `fish`, `zsh`)
- `<STACK>_USE_DOCKERFILE_LOCAL`: Whether to use Dockerfile.local by default (`true`/`false`)
- `<STACK>_OS_CUSTOM_PACKAGES`: Additional OS packages to install in base images

**RULE:** Replace `BLOGS` prefix with your stack name in uppercase.

**RULE:** This file should be gitignored as it contains developer preferences.

---

## Step 4: Copy the docker operations justfiles

Copy the following structure from the blogs example to your stack:

```
env/local/just/docker/
├── index.just              # Copy and update
├── build.just              # Copy as-is
├── run.just                # Copy as-is
├── env-files.just          # Copy as-is
└── lib/                    # Copy entire directory as-is
    ├── _build.just
    ├── _build_base_images.just
    ├── _up.just
    ├── _down.just
    ├── _run_command.just
    └── _run_image.just
```

### Update index.just

In `env/local/just/docker/index.just`, update the `default_use_dockerfile_local` variable:

```makefile
import './run.just'
import './build.just'
import './env-files.just'

restart use_dockerfile_local=default_use_dockerfile_local use_no_cache="false": \
    (down) \
    (pip-compile) \
    (build use_dockerfile_local use_no_cache) \
    (up use_dockerfile_local)
```

### Update build.just

In `env/local/just/docker/build.just`, update the variable name:

```makefile
import './env-files.just'
import './lib/_build.just'
import './lib/_build_base_images.just'

# Local variables
default_use_dockerfile_local := env_var_or_default("BLOGS_USE_DOCKERFILE_LOCAL", "false")

build use_dockerfile_local=default_use_dockerfile_local use_no_cache="false": \
    (compile-env-files) \
    (_build use_dockerfile_local use_no_cache)

build-base-images use_no_cache="false": \
    (_build_base_images use_no_cache)

_touch_compose_override:
    touch ${ROOT_DIR}/env/local/docker/docker-compose.override.yml
```

**RULE:** Update `BLOGS_USE_DOCKERFILE_LOCAL` to `<YOUR_STACK>_USE_DOCKERFILE_LOCAL`.

### Update run.just

In `env/local/just/docker/run.just`, update the shell command variable:

```makefile
import './build.just'
import './lib/_run_image.just'
import './lib/_run_command.just'
import './lib/_down.just'
import './lib/_up.just'

up use_dockerfile_local=default_use_dockerfile_local: \
    (_touch_compose_override) \
    (compile-env-files) \
    (_up use_dockerfile_local "true" "true")

down: (compile-env-files) (_down "true" "true")

shell service_name: (compile-env-files) (_run_command service_name "${BLOGS_SHELL_COMMAND}")

run_cmd service_name cmd use_dockerfile_local=default_use_dockerfile_local: \
    (compile-env-files) \
    (_run_image service_name use_dockerfile_local "true" "true" cmd)
```

**RULE:** Update `BLOGS_SHELL_COMMAND` to `<YOUR_STACK>_SHELL_COMMAND`.

---

## Available compose operation commands

Once the justfiles are set up, you can use these commands from the stack root:

### `just build [use_dockerfile_local=true/false] [use_no_cache=true/false]`

Builds all service images.

```bash
# Build using Dockerfile (production)
just build

# Build using Dockerfile.local (development)
just build use_dockerfile_local=true

# Build without cache
just build use_no_cache=true
```

**What it does:**
1. Compiles environment files (`.env.in` → `.env`)
2. Builds all services defined in docker-compose.yml
3. Uses Dockerfile.local if `use_dockerfile_local=true`

**When to use:** After changing Dockerfile, requirements, or dependencies.

### `just build-base-images [use_no_cache=true/false]`

Builds base images (e.g., `<stack>_base_python`).

```bash
just build-base-images
```

**What it does:**
1. Builds images defined in `docker-compose.base-images.yml`
2. These images are used as base for service images

**When to use:** After changing base image Dockerfiles or when setting up a new stack.

### `just up [use_dockerfile_local=true/false]`

Starts all services in detached mode.

```bash
# Start with Dockerfile.local images
just up use_dockerfile_local=true

# Start with production Dockerfiles
just up
```

**What it does:**
1. Touches docker-compose.override.yml (creates if missing)
2. Compiles environment files
3. Starts all services with docker-compose up
4. Includes src-overlays and override files

**When to use:** After building, to start the development environment.

### `just down`

Stops and removes all containers, networks.

```bash
just down
```

**What it does:**
1. Compiles environment files
2. Runs `docker compose down --remove-orphans`
3. Removes stopped containers and networks

**When to use:** To clean up the environment, before rebuilding, or when switching branches.

### `just restart [use_dockerfile_local=true/false] [use_no_cache=true/false]`

Full cycle: down → pip-compile → build → up.

```bash
# Restart with development images
just restart use_dockerfile_local=true

# Restart with fresh build
just restart use_dockerfile_local=true use_no_cache=true
```

**What it does:**
1. Stops all services (`down`)
2. Recompiles Python requirements (`pip-compile`)
3. Rebuilds images (`build`)
4. Starts services (`up`)

**When to use:** After major changes (dependencies, Dockerfile changes) or when troubleshooting.

### `just shell <service_name>`

Opens a shell in a running service container.

```bash
just shell blogs_be
```

**What it does:**
1. Compiles environment files
2. Execs into the running container
3. Uses the shell defined in `<STACK>_SHELL_COMMAND` (from `.local.env`)

**When to use:** To run commands interactively, debug, or explore the container.

**RULE:** The container must be running (`just up`) before using `just shell`.

### `just run_cmd <service_name> <cmd> [use_dockerfile_local=true/false]`

Runs a one-off command in a new container instance.

```bash
# Run Django migrations
just run_cmd blogs_be "python manage.py migrate"

# Run tests
just run_cmd blogs_be "pytest"
```

**What it does:**
1. Compiles environment files
2. Runs `docker compose run` with the specified command
3. Creates a new container (doesn't use the running one)
4. Removes container after command completes (`--rm`)

**When to use:** To run commands that shouldn't interfere with the running container, or when the service isn't up yet.

### `just compile-env-files`

Compiles `.env.in` templates to `.env` files.

```bash
just compile-env-files
```

**What it does:**
1. Touches `secrets.env` if it doesn't exist
2. Runs the Python script to compile all `.env.in` files in `env/local/docker/env_files/`
3. Substitutes variables from `secrets.env`

**When to use:** After modifying `.env.in` files or `secrets.env`.

**Note:** This command is automatically called by other commands (build, up, down, etc.), so you rarely need to run it manually.

---

## Typical workflow

### Initial setup
```bash
just build-base-images
just build use_dockerfile_local=true
just up use_dockerfile_local=true
```

### Daily development
```bash
# Start the stack
just up use_dockerfile_local=true

# Open a shell in a service
just shell blogs_be

# Inside the shell, run commands
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

### After dependency changes
```bash
just restart use_dockerfile_local=true
```

### Clean restart
```bash
just down
just build use_dockerfile_local=true use_no_cache=true
just up use_dockerfile_local=true
```

---

## Checklist

- [ ] Root `justfile` created with import statement
- [ ] `env/local/justfile` created with ROOT_DIR, COMPOSE_DIR, COMPOSE_PROJECT_NAME
- [ ] `env/local/.local.env` created with developer preferences (gitignored)
- [ ] Docker operations justfiles copied to `env/local/just/docker/`
- [ ] Variable names updated in build.just and run.just to match stack name
- [ ] All commands tested: `build`, `build-base-images`, `up`, `down`, `restart`, `shell`, `run_cmd`, `compile-env-files`
- [ ] Developers can successfully start the stack with `just up`
- [ ] Shell access works with `just shell <service_name>`
