class Rel:
    def __init__(self, fact_bits=None, verb=None, args=None, kwargs=None):
        self.fact_bits = fact_bits or tuple()
        self.verb = verb
        self.args = args or ()
        self.kwargs = kwargs or {}

    def __getattr__(self, name):
        def relates_to(other_entity=None):
            self.fact_bits = (
                *self.fact_bits,
                name,
                *([] if other_entity is None else [other_entity]),
            )
            return self

        return relates_to

    def __str__(self):
        if self.verb:
            formatted_args = ", ".join(str(arg) for arg in self.args)
            formatted_kwargs = ", ".join(f"{k}={v}" for k, v in self.kwargs.items())
            infix = ", " if self.args and self.kwargs else ""
            params = formatted_args + infix + formatted_kwargs
            return f"{self.verb}({params})"
        elif self.fact_bits:
            from sunya.steps.rules.rel_to_string import rel_to_string
            return rel_to_string(self)
        return ""
