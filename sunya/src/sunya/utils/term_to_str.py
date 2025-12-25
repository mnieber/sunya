from multimethods import MultiMethod, Default


def dispatch_term_to_str(x):
    return (type(x),)


term_to_str = MultiMethod("term_to_str", dispatch_term_to_str)


@term_to_str.method(Default)
def default_to_str(term):
    return f"?:{term.__class__.__name__}"
