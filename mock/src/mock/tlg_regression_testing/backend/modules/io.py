from mock.default.stack.namespace import Module
from mock.default.backend.namespace import Action, Model
from sunya import use_spec
import sunya.spec as spec


class IO(Module):
    @use_spec(spec.backend_model)
    class Models:
        class S3Client(Model):
            bucket_name: str

        class ExampleRepository(Model):
            geomodel_name: str
            examples: list["IO.Models.Example"] = []

        class ExampleRepositoryStat(Model):
            nr_of_stored_examples_by_selector_name: dict[str, int]

        class Example(Model):
            selector_name: str
            hash: str
            slot_nr: int
            input_json: str
            output_json: str

    @use_spec(spec.backend_action)
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
