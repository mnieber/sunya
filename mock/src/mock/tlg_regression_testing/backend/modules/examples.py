from mock.default.backend.namespace import Action, Model
from mock.default.stack.namespace import Module


class Examples(Module):
    class Models:
        class ExampleRepository(Model):
            geomodel_name: str
            examples: list["Examples.Models.Example"] = []

        class ExampleRepositoryStat(Model):
            nr_of_stored_examples_by_selector_name: dict[str, int]

        class Example(Model):
            selector_name: str
            hash: str
            slot_nr: int
            input_json: str
            output_json: str

    class Actions:
        class ClearExamples(Action):
            pass

        class DownloadExamples(Action):
            pass

        class DownloadExampleRepository(Action):
            pass

        class DownloadExampleRepositoryStat(Action):
            pass

        class UploadExample(Action):
            pass
