class GlobalNamespace:
    def __init__(self):
        self._attributes = {}

    def __setattr__(self, name, value):
        if name == "_attributes":
            super().__setattr__(name, value)
        elif name in self._attributes:
            raise AttributeError(f"Attribute '{name}' already exists")
        else:
            self._attributes[name] = value

    def __getattr__(self, name):
        if name in self._attributes:
            return self._attributes[name]
        raise AttributeError(f"Attribute '{name}' does not exist")


G = GlobalNamespace()
