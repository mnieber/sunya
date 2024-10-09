from default.stack.namespace import Module
from default.backend.namespace import Action
from sunya import G as g, use_spec
import sunya.spec as spec


class Collect(Module):
    @use_spec(spec.backend_action)
    class Actions:
        class CollectRegressionTestingExamples(Action):
            pass


g.collect_regression_testing_examples_action = (
    Collect.Actions.CollectRegressionTestingExamples()
)
