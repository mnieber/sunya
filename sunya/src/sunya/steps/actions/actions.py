from sunya.steps.models.rel import Rel


class Actions:
    def calls(self, *args, **kwargs):
        return Rel(verb="calls", args=args, kwargs=kwargs)

    def returns(self, *args):
        return Rel(verb="returns", args=args)

    def creates(self, *args):
        return Rel(verb="creates", args=args)

    def it(self, rel: Rel):
        return rel


actions = Actions()
