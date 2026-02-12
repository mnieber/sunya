from darshana_be.actors.actions.create_actor import CreateActorForm
from darshana_be.actors.models import Actor, Role
from darshana_be.common.form_serializer import FormSerializer
from darshana_be.common.serializers import BaseModelSerializer, ReadSerializerMixin
from darshana_be.actors.actions.create_role import CreateRoleForm


class ActorSerializer(ReadSerializerMixin, BaseModelSerializer):
    class Meta:
        model = Actor
        fields = ["id", "key"]


class CreateActorFormSerializer(FormSerializer):
    class Meta:
        form_class = CreateActorForm


class RoleSerializer(ReadSerializerMixin, BaseModelSerializer):
    class Meta:
        model = Role
        fields = ["id", "name"]


class CreateRoleFormSerializer(FormSerializer):
    class Meta:
        form_class = CreateRoleForm
