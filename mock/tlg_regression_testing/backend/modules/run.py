from default.stack.namespace import Module, Function
from sunya import EntityWithId, actor_to_str, G as g


class Run(Module):
    class Models:
        class TestResult(EntityWithId):
            selector: str
            input_id: str
            passed: bool
            diff: str = ""

    class Functions:
        class RunRegressionTests(Function):
            pass

        class GenerateHtmlReport(Function):
            pass


g.run_regression_tests_function = Run.Functions.RunRegressionTests()
g.generate_html_report_function = Run.Functions.GenerateHtmlReport()


@actor_to_str.method((Run.Models.TestResult,))
def test_result_to_str(result):
    return f"{result.selector}-{result.input_id}+:test_result"
