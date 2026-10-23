import typing as T


class GlobalNamespace:
    def __init__(self):
        self._attributes = {}

    def clear(self):
        """Clear all global namespace attributes."""
        self._attributes = {}

    def set(self, name, value, force=False):
        if name in self._attributes and not force:
            raise AttributeError(f"Attribute '{name}' already exists")
        self._attributes[name] = value

    def __setattr__(self, name, value):
        if name in ("_attributes", "resolver_fn"):
            super().__setattr__(name, value)
        else:
            self.set(name, value)

    def __getattr__(self, name):
        if name not in self._attributes:
            raise GlobalNamespaceEntityNotFound(name)

        return T.cast(T.Any, self._attributes[name])


G = GlobalNamespace()


class GlobalNamespaceEntityNotFound(Exception):
    pass


class GlobalNamespaceMisconfigured(Exception):
    pass
