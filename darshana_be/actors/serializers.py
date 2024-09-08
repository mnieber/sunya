from actors.actions.create_actor import CreateActorForm
from actors.models import Actor
from common.form_serializer import FormSerializer
from common.serializers import BaseModelSerializer, ReadSerializerMixin


class ActorSerializer(ReadSerializerMixin, BaseModelSerializer):
    class Meta:
        model = Actor
        fields = ["id", "key"]


class CreateActorFormSerializer(FormSerializer):
    class Meta:
        form_class = CreateActorForm
