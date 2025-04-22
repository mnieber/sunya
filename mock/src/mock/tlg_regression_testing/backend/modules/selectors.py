import typing as T

import sunya.spec as spec
from mock.default.backend.namespace import Action
from mock.default.stack.namespace import Module
from sunya import EntityWithId, use_spec


class Selectors(Module):
    @use_spec(spec.backend_model)
    class Models:
        class Selector(EntityWithId):
            name: str
            nr_of_examples: int
            func: callable = None

        class SelectorsRepository(EntityWithId):
            selectors: T.List["Selectors.Models.Selector"] = []

    @use_spec(spec.backend_action)
    class Actions:
        class RegisterSelector(Action):
            """
            A decorator function that registers selector functions for regression testing.
            Each selector identifies examples that should be collected for regression testing.
            """

        class ImportSelectors(Action):
            """
            Imports selector modules from a specified path.
            """
