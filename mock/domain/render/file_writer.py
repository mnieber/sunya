from pathlib import Path


class FileWriter:
    def __init__(self):
        self.output_dir = Path(".output")

    def write_module_spec(self, module_name, module_spec_md):
        fn = self._get_fn(["modules", module_name], "spec.md")
        self._write_file(fn, module_spec_md)

    def write_scenario(self, scenario_name, scenario_md):
        fn = self._get_fn(["scenarios"], f"{scenario_name}.md")
        self._write_file(fn, scenario_md)

    def _get_fn(self, dir_names, name):
        output_dir = self.output_dir
        for dir_name in dir_names:
            output_dir = output_dir / dir_name
            output_dir.mkdir(exist_ok=True)
        return output_dir / name

    def _write_file(self, fn, content):
        with open(fn, "w") as f:
            for line in content.split("\n"):
                f.write(line.rstrip() + "\n")
