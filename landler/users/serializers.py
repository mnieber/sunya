from common.form_serializer import FormSerializer
from common.serializers import BaseModelSerializer, ReadOnlySerializerMixin
from users.actions.create_user import CreateUserForm
from users.models import User


class CreateUserFormSerializer(FormSerializer):
    class Meta:
        form_class = CreateUserForm


class UserSerializer(ReadOnlySerializerMixin, BaseModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
