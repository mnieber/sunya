def use_spec(create_spec):
    def decorator(cls):
        cls._create_spec = create_spec
        return cls

    return decorator
