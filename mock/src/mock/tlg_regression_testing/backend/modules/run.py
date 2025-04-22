from mock.default.backend.namespace import Action
from mock.default.stack.namespace import Module


class Run(Module):
    class Actions:
        class RunRegressionTests(Action):
            pass

        class GenerateHtmlReport(Action):
            pass
