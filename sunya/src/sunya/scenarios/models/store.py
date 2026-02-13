import typing as T

from dataclassy import dataclass

if T.TYPE_CHECKING:
    from sunya.scenarios.models.component import Component


@dataclass(kw_only=True)
class Store:
    components: T.List["Component"] = []

    def reset(self):
        from sunya.modules.utils.module_namespace import M
        from sunya.scenarios.utils.global_namespace import G  # noqa

        self.components.clear()
        M.clear()
        G.clear()

    @property
    def component(self):
        return self.components[-1]

    @property
    def scenario(self):
        return self.component.scenario


store = Store()


def get_store():
    global store
    return store
