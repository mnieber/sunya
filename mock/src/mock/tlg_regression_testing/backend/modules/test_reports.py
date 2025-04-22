import typing as T

from mock.default.backend.namespace import Action, Model
from mock.default.stack.namespace import Module


class TestReport(Module):
    class Models:
        class TestReport(Model):
            """
            Contains test results and differences between expected and actual outputs.
            """

            app_id: str
            diffs: T.List["TestReport.Models.TestReportDiff"] = []

        class TestReportDiff(Model):
            """
            Contains the difference between expected and actual outputs for a single test.
            """

            example_hash: str
            input_data_json: str
            diff_html: str

    class Actions:
        class WriteTestReport(Action):
            """
            Writes a test report to a file.
            """


        class ExportTestReportAsHtml(Action):
            """
            Exports a test report as HTML.
            """


        class UpdateTestReport(Action):
            """
            Updates a test report with the result of a regression test.
            """

