from pathlib import Path


class FileWriter:
    def __init__(self, output_dir):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True, parents=True)

    def write_scenario(self, package, scenario, scenario_md):
        fn = self._get_fn([package, "scenarios"], scenario.name + ".md")
        self._write_file(fn, scenario_md)
        return fn

    def write_module(self, package, module_name, module_md):
        fn = self._get_fn([package, "modules"], module_name + ".md")
        self._write_file(fn, module_md)

    def _get_fn(self, dir_names, name):
        result = Path(self.output_dir)
        for dir_name in dir_names:
            result = result / dir_name
        result.mkdir(parents=True, exist_ok=True)
        return result / name

    def _write_file(self, fn, content):
        with open(fn, "w") as f:
            f.write(content)
