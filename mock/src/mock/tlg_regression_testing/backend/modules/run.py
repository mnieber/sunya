import typing as T

from mock.default.backend.namespace import Action, Model
from mock.default.stack.namespace import Module


class Run(Module):
    class Models:
        class RunTimeData(Model):
            app_id: str
            input_data: T.Any
            output_data: T.Any
            extra_data: T.Any
            test_report: "TestReport.Models.TestReport"

            @property
            def has_output_data(self) -> bool:
                pass

            @property
            def example_hash(self) -> str:
                pass

        class Cache(Model):
            data_by_key: T.Dict[str, T.Any]

            def get_item(self, key: str, fallback_item=None):
                pass

            def set_item(self, key: str, data: T.Any):
                pass

            def clear(self):
                pass

    class Actions:
        class RunRegressionTests(Action):
            pass

        class GenerateHtmlReport(Action):
            pass

        class CollectExample(Action):
            pass

        class CreateRunTimeData(Action):
            pass

        class CreateExample(Action):
            pass

        class RunRegressionTest(Action):
            pass

        class DropExample(Action):
            pass

        class UpdateExample(Action):
            pass

    class Rules:
        class GetMatchingSelectors(Action):
            pass

        class IsCollectingRtestExamplesEnabled(Action):
            pass

    class Utils:
        class IsRunningRegressionTest(Action):
            pass

    class Errors:
        class NoRunTimeDataError(Exception):
            pass
