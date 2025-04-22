import typing as T

from mock.default.backend.namespace import Action, Model
from mock.default.stack.namespace import Module


class Examples(Module):
    class Models:
        class ExampleRepository(Model):
            app_id: str
            examples: list["Examples.Models.Example"] = []

        class ExampleRepositoryStat(Model):
            nr_of_stored_examples_by_selector_name: dict[str, int]

        class Example(Model):
            hash: str
            input_data: T.Dict[str, T.Any]
            output_data: T.Dict[str, T.Any]
            cached_data_by_key: T.Dict[str, T.Any]

        class ExampleSlot(Model):
            example_hash: str
            selector_name: str
            app_id: str

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

        class WriteExample(Action):
            pass

        class WriteExampleSlot(Action):
            pass

        class MaybeAddExample(Action):
            pass

        class DropExample(Action):
            pass

        class UpdateExample(Action):
            pass

    class Rules:
        class GetExampleFn(Action):
            pass

        class GetExampleSlotFn(Action):
            pass

    class Errors:
        class RegressionTestExampleNotFoundError(Exception):
            pass

        class UpdatedExampleOutputNotFoundError(Exception):
            pass
