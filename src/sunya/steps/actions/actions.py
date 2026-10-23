from sunya.steps.models.rel import Rel


class Actions:
    def calls(self, *args, **kwargs):
        return Rel(verb="calls", args=args, kwargs=kwargs)

    def returns(self, *args, **kwargs):
        return Rel(verb="returns", args=args, kwargs=kwargs)

    def creates(self, *args, **kwargs):
        return Rel(verb="creates", args=args, kwargs=kwargs)

    def it(self, rel: Rel):
        return rel


actions = Actions()
