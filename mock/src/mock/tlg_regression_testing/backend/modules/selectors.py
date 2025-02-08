from mock.default.stack.namespace import Module
from mock.default.backend.namespace import Action
from sunya import EntityWithId, use_spec
import sunya.spec as spec


class Selectors(Module):
    @use_spec(spec.backend_model)
    class Models:
        class Selector(EntityWithId):
            name: str
            num_examples: int

        class SelectorsRepository(EntityWithId):
            selectors: list["Selectors.Models.Selector"] = []

    @use_spec(spec.backend_action)
    class Actions:
        class RegisterSelector(Action):
            pass
