import importlib
import inspect


def get_class_source(klass):
    try:
        source = inspect.getsource(klass)
        return source
    except TypeError:
        print(f"The object {klass} is not a class.")
    except OSError:
        print(f"Source code for {klass} could not be found.")


def find_root_class(cls, base_cls):
    if not isinstance(cls, type):
        raise TypeError(f"Arg cls ({cls}) must be a class")

    target = cls
    while target and isinstance(target, type):
        if issubclass(target, base_cls):
            return target
        if not target.__bases__:
            target = None
        else:
            module = importlib.import_module(target.__module__)
            parts = target.__qualname__.split(".")[:-1]
            target = module
            for part in parts:
                target = getattr(target, part)
    return None
