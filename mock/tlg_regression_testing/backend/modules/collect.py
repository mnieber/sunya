from default.stack.namespace import Module, Function
from sunya import G as g


class Collect(Module):
    class Functions:
        class CollectRegressionTestingExamples(Function):
            pass


g.collect_regression_testing_examples_function = (
    Collect.Functions.CollectRegressionTestingExamples()
)
