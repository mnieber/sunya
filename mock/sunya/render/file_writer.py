from pathlib import Path


class FileWriter:
    def __init__(self, output_dir):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

    def write_module_spec(self, module_name, module_spec_md):
        parts = module_name.split("/")
        fn = self._get_fn([*parts[:-1], "modules"], f"{parts[-1]}.yaml")
        self._write_file(fn, module_spec_md)

    def write_scenario(self, scenario_name, scenario_md):
        parts = scenario_name.split("/")
        fn = self._get_fn([*parts[:-1], "scenarios"], f"{parts[-1]}.yaml")
        self._write_file(fn, scenario_md)

    def _get_fn(self, dir_names, name):
        return self.output_dir / "-".join([*dir_names, name])

    def _write_file(self, fn, content):
        with open(fn, "w") as f:
            for line in content.split("\n"):
                f.write(line.rstrip() + "\n")
