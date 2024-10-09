from default.stack.namespace import Module, Function
from sunya import EntityWithId, actor_to_str, G as g


class Selectors(Module):
    class Models:
        class Selector(EntityWithId):
            name: str
            num_examples: int

        class SelectorsRepository(EntityWithId):
            selectors: list["Selectors.Models.Selector"] = []

    class Functions:
        class RegisterSelector(Function):
            pass


g.selectors_repository = Selectors.Models.SelectorsRepository()
g.register_selector = Selectors.Functions.RegisterSelector()


@actor_to_str.method((Selectors.Models.Selector,))
def selector_to_str(selector):
    return f"{selector.name}+:selector"


@actor_to_str.method((Selectors.Models.SelectorsRepository,))
def selectors_repository_to_str(repo):
    return "selectors_repository+:selectors_repository"
