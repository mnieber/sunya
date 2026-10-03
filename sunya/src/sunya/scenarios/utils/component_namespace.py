class ComponentNamespace:
    """
    The component namespace (m) stores dynamically created component specs.
    An entry follows the pattern: m.<component_name>.<module_name>.<section_name>.<actor_name>

    Example: m.WebServer.Projects.Rules.GetFoo declares:
      - A WebServer component exists
      - With a Projects module
      - With a Rules section
      - With a GetFoo actor
    """

    def __init__(self):
        self._components = {}

    def clear(self):
        """Clear all component specs."""
        self._components = {}

    def __getattr__(self, name: str) -> ComponentSpec:
        """Get or create a component spec."""
        if name.startswith("_"):
            raise AttributeError(
                f"'{type(self).__name__}' object has no attribute '{name}'"
            )

        if name not in self._components:
            self._components[name] = ComponentSpec(name)

        return self._components[name]


class ComponentSpec:
    """Represents a component (e.g., Projects in m.Projects)."""

    def __init__(self, component_name: str):
        self._component_name = component_name
        self._modules = {}

    def __getattr__(self, name: str):
        """Get or create a modules in this component."""
        if name.startswith("_"):
            raise AttributeError(
                f"'{type(self).__name__}' object has no attribute '{name}'"
            )

        if name not in self._modules:
            self._modules[name] = ModuleSpec(self._component_name, name)

        return self._modules[name]


class ModuleSpec:
    """Represents a module (e.g., Projects in m.Projects)."""

    def __init__(self, module_name: str):
        self._module_name = module_name
        self._sections = {}

    def __getattr__(self, name: str):
        """Get or create a section in this module."""
        if name.startswith("_"):
            raise AttributeError(
                f"'{type(self).__name__}' object has no attribute '{name}'"
            )

        if name not in self._sections:
            self._sections[name] = SectionSpec(self._module_name, name)

        return self._sections[name]


class SectionSpec:
    """Represents a section within a module (e.g., Rules in Projects.Rules)."""

    def __init__(self, module_name: str, section_name: str):
        self._module_name = module_name
        self._section_name = section_name
        self._actors = {}

    def __getattr__(self, name: str):
        """Get or create an actor in this section."""
        if name.startswith("_"):
            raise AttributeError(
                f"'{type(self).__name__}' object has no attribute '{name}'"
            )

        if name not in self._actors:
            # Create a placeholder actor - could be a string or a more complex object
            self._actors[name] = ActorSpec(self._module_name, self._section_name, name)

        return self._actors[name]


class ActorSpec:
    """Represents an actor within a section."""

    def __init__(self, module_name: str, section_name: str, actor_name: str):
        self._module_name = module_name
        self._section_name = section_name
        self._actor_name = actor_name

    @property
    def full_path(self) -> str:
        """Returns the full module spec path (e.g., 'Jobs.Actors.Scheduler')."""
        return f"{self._module_name}.{self._section_name}.{self._actor_name}"

    def __repr__(self):
        return self.full_path


C = ComponentNamespace()
