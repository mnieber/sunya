def note_over(actor: any, note: any):
    actors = actor if isinstance(actor, list) else [actor]
    actor_names = ", ".join(a.name for a in actors)
    return f"note over {actor_names}: {note}"
