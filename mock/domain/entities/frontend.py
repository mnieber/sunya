from sunya import Entity, actor_to_str


class Frontend(Entity):
    pass


frontend = Frontend()


@actor_to_str.method((Frontend,))
def frontend_to_str(frontend):
    return f":frontend"
