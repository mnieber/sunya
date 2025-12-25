class Rel:
    def __init__(self, fact_bits=None):
        self.fact_bits = fact_bits or tuple()

    def __getattr__(self, name):
        def relates_to(other_entity=None):
            self.fact_bits = (
                *self.fact_bits,
                name,
                *([] if other_entity is None else [other_entity]),
            )
            return self

        return relates_to
