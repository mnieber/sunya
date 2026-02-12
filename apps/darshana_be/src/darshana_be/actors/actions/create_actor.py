from darshana_be.actors.models import Actor
from dataclassy import dataclass


@dataclass
class CreateActorForm:
    key: str


def create_actor(create_actor_form: CreateActorForm):
    _validate_args(create_actor_form)

    actor = Actor(
        key=create_actor_form.key,
    )
    actor.save()

    return actor


def _validate_args(create_actor_form: CreateActorForm):
    if Actor.objects.filter(key=create_actor_form.key).exists():
        raise ActorWithKeyAlreadyExistsError()


class ActorWithKeyAlreadyExistsError(Exception):
    pass
