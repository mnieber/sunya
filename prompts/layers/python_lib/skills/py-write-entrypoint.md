# Skill: py-write-entrypoint

Applies when writing an application entrypoint.

Primary reference: `bookie/runtime/entrypoints/bookie.py`, `bookie/pyproject.toml`

---

## File location

```
<app_package>/runtime/entrypoints/<name>.py
```

## Structure

An entrypoint file contains:

1. A `_parse_args()` function using `argparse`.
2. Any private helper functions needed by `main()`.
3. A `main()` function that calls `_parse_args()` and dispatches to actions.
4. A `if __name__ == "__main__": sys.exit(main())` guard.

RULE: Use a separate `_parse_args()` function based on the `argparse` package.

```python
def _parse_args():
    parser = argparse.ArgumentParser(description="...")
    # add arguments / subparsers
    return parser.parse_args()


def main():
    args = _parse_args()
    # dispatch to actions
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

## Registering in pyproject.toml

RULE: Add the entrypoint to the `[project.scripts]` section of `pyproject.toml`.

```toml
[project.scripts]
bookie = "bookie.runtime.entrypoints.bookie:main"
```

## Checklist

- [ ] Entrypoint file is under `<app_package>/runtime/entrypoints/`
- [ ] `_parse_args()` uses `argparse` and is a private function (leading underscore)
- [ ] `main()` calls `_parse_args()` and dispatches to action functions
- [ ] `if __name__ == "__main__": sys.exit(main())` guard present
- [ ] Entry added to `[project.scripts]` in `pyproject.toml`
