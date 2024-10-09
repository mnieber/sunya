from default.stack.namespace import Module
from default.backend.namespace import Action
from sunya import EntityWithId, actor_to_str, G as g, use_spec
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


g.selectors_repository = Selectors.Models.SelectorsRepository()
g.register_selector_action = Selectors.Actions.RegisterSelector()


@actor_to_str.method((Selectors.Models.Selector,))
def selector_to_str(selector):
    return f"{selector.name}+:selector"


@actor_to_str.method((Selectors.Models.SelectorsRepository,))
def selectors_repository_to_str(repo):
    return "selectors_repository+:selectors_repository"
