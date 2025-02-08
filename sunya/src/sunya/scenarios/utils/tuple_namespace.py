class TupleBuilder:
    def __init__(self, tupl=None):
        self.tupl = tupl or tuple()

    def __getattr__(self, name):
        def relates_to(*other_entities):
            self.tupl = (*self.tupl, name, *other_entities)
            return self

        return relates_to

    def __iter__(self):
        return iter(self.tupl)


class TupleNamespace:
    def __getattr__(self, name):
        tuple_builder = TupleBuilder()
        return getattr(tuple_builder, name)


I = TupleNamespace()
