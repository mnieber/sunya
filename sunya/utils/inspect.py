import importlib


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


def get_cls_members(container):
    classes = []
    for cls_name, cls in container.__dict__.items():
        if cls_name.startswith("_"):
            continue
        classes.append((cls_name, cls))
    return classes
