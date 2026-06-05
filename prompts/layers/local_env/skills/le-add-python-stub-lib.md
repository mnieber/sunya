# Skill: le-add-python-stub-lib

Applies when adding a Python library stub to the stack that references external library code stored outside the stack directory.

Primary reference: `examples/blogs/src/libs/woodstock/`

---

## What is a stub library?

A stub library is a minimal Python package structure in `<stack>/src/libs/` that acts as a placeholder for a real library whose source code lives elsewhere (e.g., in a separate repository or development directory).

**Purpose:**

- Allows the library to be installed in Docker images during build
- Defines the library's dependencies in `pyproject.toml`
- The actual source code is overlaid at runtime via `docker-compose.override.yml`
- Enables local development of both the stack and the library simultaneously

**When to use:**

- Library is developed in a separate repository

---

## File structure

A stub library contains only the minimal files needed for Python packaging:

```
<stack>/src/libs/<lib_name>/
├── pyproject.toml          # Package metadata and dependencies
├── setup.py                # Placeholder creation script
├── README.md               # Minimal library description
└── src/
    └── <lib_name>/
        └── __init__.py     # Placeholder module
```

Example for `woodstock`:

```
src/libs/woodstock/
├── pyproject.toml
├── setup.py
├── README.md
└── src/
    └── woodstock/
        └── __init__.py
```

---

## Step 1: Create the directory structure

Create the stub library directory:

```bash
mkdir -p src/libs/woodstock/src/woodstock
```

**RULE:** Use `src/<lib_name>/` layout (src-layout) inside the stub, not flat layout.

---

## Step 2: Create pyproject.toml

The `pyproject.toml` file must contain the **actual dependencies** of the real library:

```toml
[project]
name = "woodstock"
version = "0.1.0"
readme = "README.md"
dependencies = ["dataclassy", "boto3", "bottle"]

[project.optional-dependencies]
test = ["pytest>=7.0.0", "pytest-cov>=4.0.0", "moto[s3]>=4.0.0"]

[project.scripts]
woodstock = "woodstock.server.entrypoints.woodstock:main"

[tool.setuptools.package-dir]
"" = "src"

[tool.setuptools.packages.find]
where = ["src"]

[build-system]
requires = ["setuptools>=45", "wheel"]
build-backend = "setuptools.build_meta"
```

### Key sections

**dependencies:** List all runtime dependencies the real library needs

```toml
dependencies = ["dataclassy", "boto3", "bottle"]
```

**RULE:** These must match the real library's dependencies exactly. When the real library adds dependencies, update this stub.

**optional-dependencies:** Development and testing dependencies

```toml
[project.optional-dependencies]
test = ["pytest>=7.0.0", "pytest-cov>=4.0.0", "moto[s3]>=4.0.0"]
```

**scripts:** Entry points if the library provides CLI commands

```toml
[project.scripts]
woodstock = "woodstock.server.entrypoints.woodstock:main"
```

Only include if the real library has entry points.

**package-dir:** Use src-layout

```toml
[tool.setuptools.package-dir]
"" = "src"
```

**RULE:** The stub's pyproject.toml should be kept in sync with the real library's pyproject.toml, especially the dependencies section.

---

## Step 3: Create setup.py

Create a `setup.py` that generates a placeholder package:

```python
from pathlib import Path

from setuptools import setup


def create_placeholder():
    this_directory = Path(__file__).parent
    pkg_directory = this_directory / "src" / "woodstock"

    if not pkg_directory.exists():
        pkg_directory.mkdir(parents=True)
        with open(pkg_directory / "__init__.py", "w") as f:
            f.write("# Placeholder for package")


if __name__ == "__main__":
    create_placeholder()
    setup()
```

**What this does:**

1. Creates the package directory if it doesn't exist
2. Creates a placeholder `__init__.py` file
3. Calls `setup()` to install the package

**RULE:** Replace `woodstock` with your actual library name in the path.

---

## Step 4: Create README.md

Create a minimal README:

```markdown
# woodstock
```

Just the library name. The real documentation lives with the real library.

---

## Step 5: Create the placeholder **init**.py

Create `src/<lib_name>/__init__.py`:

```python
# Placeholder for the real library
```

This file will be overwritten when the real library code is overlaid at runtime.

---

## Step 6: Reference in service requirements.editable

Services that use the stub library must reference it in their `requirements.editable` file:

In `<stack>/src/services/<service_name>/requirements.editable`:

```
-e ${BLOGS_LIBS_DIR}/woodstock
```

**RULE:** Use the `<STACK>_LIBS_DIR` environment variable to reference the library location.

**RULE:** The `-e` flag installs in editable mode, allowing the overlay to take effect.

This file is used during `just pip-compile` to include the library in `requirements.txt`.

---

## Step 7: Copy stub library files in Dockerfile

Services must copy the stub library's metadata files in their Dockerfiles:

### In Dockerfile.local:

```dockerfile
# Copy the requirements file(s) for each library
COPY libs/woodstock/pyproject.toml libs/woodstock/setup.py libs/woodstock/README.md /app/libs/woodstock/
```

Only copy the minimal files needed for installation, not the source code.

### In Dockerfile:

```dockerfile
# Copy each library
COPY libs/woodstock /app/libs/woodstock
```

Copy the full stub directory for production builds.

**RULE:** In Dockerfile.local, only copy metadata files (pyproject.toml, setup.py, README.md). The source code is overlaid at runtime.

**RULE:** In Dockerfile, copy the entire stub directory.

---

## Step 8: Overlay real library code in docker-compose.override.yml

To use the real library code during development, add a volume mount in `docker-compose.override.yml`:

```yaml
services:
  blogs_be:
    volumes:
      # Lib code overlays
      - /home/maarten/projects/woodstock/src/libs/woodstock:/app/libs/woodstock
```

**Path structure:** The real library should also use src-layout:

```
/home/maarten/projects/woodstock/
└── src/
    └── libs/
        └── woodstock/
            ├── __init__.py
            ├── server/
            └── ...
```

This mounts the real library's source code over the placeholder stub in the container.

**RULE:** Use absolute paths in `docker-compose.override.yml` since it's developer-specific.

**RULE:** The real library must have the same package structure as expected by the stub.

---

## Step 9: Add to docker-compose.src-overlays.yml

Add the stub library overlay to `docker-compose.src-overlays.yml`:

```yaml
services:
  blogs_be:
    volumes:
      - ${ROOT_DIR}/src/services/blogs_be:/app/src
      - ${ROOT_DIR}/src/libs/woodstock:/app/libs/woodstock
```

This ensures the stub is available even when the real library isn't overlaid.

**RULE:** This overlay is for the stub itself, not the real library. The real library overlay goes in `docker-compose.override.yml`.

---

## How it works

### During Docker build:

1. Stub library metadata files are copied into the image
2. `pip install -e /app/libs/woodstock` installs the stub in editable mode
3. This installs the dependencies listed in the stub's `pyproject.toml`
4. The placeholder `__init__.py` is present but not used

### During container runtime:

1. If no overlay in `docker-compose.override.yml`: the stub's placeholder code is used (minimal functionality)
2. If overlay configured: the real library code is mounted over `/app/libs/woodstock`, replacing the placeholder
3. The editable install means Python immediately sees the real library code
4. Dependencies are already installed from the stub's `pyproject.toml`

### Benefits:

- No rebuild needed when editing library code
- Library dependencies are baked into the image
- Works whether or not the real library is available
- Multiple developers can have different library paths

---

## Keeping stub in sync with real library

When the real library changes dependencies:

1. Update the stub's `pyproject.toml` to match
2. Run `just pip-compile` in the service
3. Rebuild the service image: `just build use_dockerfile_local=true`

**RULE:** The stub's `pyproject.toml` dependencies must match the real library's dependencies.

---

## Checklist

- [ ] Stub directory created at `src/libs/<lib_name>/`
- [ ] `pyproject.toml` created with correct dependencies matching real library
- [ ] `setup.py` created with placeholder generation logic
- [ ] `README.md` created with library name
- [ ] Placeholder `src/<lib_name>/__init__.py` created
- [ ] Service's `requirements.editable` references stub with `${<STACK>_LIBS_DIR}`
- [ ] Service's `Dockerfile.local` copies stub metadata files only
- [ ] Service's `Dockerfile` copies full stub directory
- [ ] Stub overlaid in `docker-compose.src-overlays.yml`
- [ ] Real library code overlaid in `docker-compose.override.yml` (developer-specific)
- [ ] Real library uses same src-layout structure
