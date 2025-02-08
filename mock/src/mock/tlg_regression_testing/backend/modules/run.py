from mock.default.stack.namespace import Module
from mock.default.backend.namespace import Action
from sunya import EntityWithId, use_spec
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
