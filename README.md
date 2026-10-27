# Sunya

## Configuration

Sunya is configured with a YAML file. When no `--config` option is given,
`sunya render` and `sunya serve` look in the current directory for (in order)
`sunya.config.yaml`, `sunya.config.yml`, `.sunya.yaml` or `.sunya.yml`.

### Component configs

A component config describes the spec files of a single component and where
the rendered documentation should be written:

```yaml
output_dir: ../../doc/spec
component_name: jogger
package_config_by_name:
  jogger:
    output_dir: .
    scenario_paths:
      - scenarios/**/scenario.py
```

- `component_name`: the name of the component in the spec store.
- `output_dir`: where rendered documentation is written. A relative path is
  resolved against the config file's directory (or against `root_dir`, if set).
- `root_dir` (optional): the directory that contains the spec files, relative
  to the config file. Defaults to the directory of the config file.
- `package_config_by_name`: per package, the glob patterns of its scenario
  files (relative to `root_dir`) and an optional `output_dir` (relative to the
  component's `output_dir`, defaulting to the package name).

### Referencing other configs

A config can reference other config files with the `configs` key. This lets you
keep a config next to each component (service, library, ...) and use a single
top-level config to render all of them at once:

```yaml
configs:
  - src/services/backend/extra/spec_src/sunya.config.yaml
  - src/services/frontend/extra/spec_src/sunya.config.yaml
  - src/libs/jogger/extra/spec_src/sunya.config.yaml
  - ~/projects/woodstock/src/libs/woodstock/extra/spec_src/sunya.config.yaml
output_dir: /opt/projects/calcium/browse
```

When Sunya loads a config, it also loads every config listed under `configs`,
recursively (a referenced config may itself have a `configs` key). The rules
are:

- Paths in `configs` may be relative, absolute, start with `~`, or contain
  environment variables (e.g. `$HOME/...`). Relative paths are resolved against
  the directory of the config that references them.
- Each referenced config is processed on its own: its `output_dir`, `root_dir`
  and scenario paths are resolved relative to its own location, and its
  documentation is written to its own `output_dir`. Configs can therefore live
  in different repositories.
- A config that has no `package_config_by_name` (such as the top-level config
  above) renders no specs itself; it only serves to collect other configs.
- All components end up in one shared spec store, so scenarios of different
  components are rendered together.
- The `output_dir` of the top-level config is where
  `sunya render --create-simple-output-dir` writes the combined `store`
  directory (`store/<component_name>/scenarios/<scenario_name>.md`), and where
  `sunya serve` serves it from.
- In watch mode (`sunya render --watch`), the spec files of all collected
  configs are watched.
- A missing config file, invalid YAML or a circular reference between configs
  is reported as an error.
