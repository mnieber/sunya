import pytest
from darshana_be.actors.tests.factories import ActorFactory

from darshana_be.actors.actions.create_actor import (
    ActorWithKeyAlreadyExistsError,
    CreateActorForm,
    create_actor,
)


class TestCreateActorAction:
    @pytest.mark.django_db
    def test_create_actor_action_success(self):
        # Given
        create_actor_form = CreateActorForm(key="test_actor")

        # When
        actor = create_actor(create_actor_form)

        # Then
        assert actor.key == "test_actor"

    @pytest.mark.django_db
    def test_create_actor_action_with_existing_key(self):
        # Given
        ActorFactory(key="existing_actor")

        create_actor_form = CreateActorForm(key="existing_actor")

        # When / Then
        with pytest.raises(ActorWithKeyAlreadyExistsError):
            create_actor(create_actor_form)
