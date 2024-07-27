from yaml import dump


def dict2yaml(x):
    return dump(x, sort_keys=False)
