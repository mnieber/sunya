from default.stack.namespace import Module
from default.backend.namespace import Action
from sunya import EntityWithId, actor_to_str, G as g, use_spec
import sunya.spec as spec


class Run(Module):
    @use_spec(spec.backend_model)
    class Models:
        class TestResult(EntityWithId):
            selector: str
            input_id: str
            passed: bool
            diff: str = ""

    @use_spec(spec.backend_action)
    class Actions:
        class RunRegressionTests(Action):
            pass

        class GenerateHtmlReport(Action):
            pass


g.run_regression_tests_action = Run.Actions.RunRegressionTests()
g.generate_html_report_action = Run.Actions.GenerateHtmlReport()


@actor_to_str.method((Run.Models.TestResult,))
def test_result_to_str(result):
    return f"{result.selector}-{result.input_id}+:test_result"
