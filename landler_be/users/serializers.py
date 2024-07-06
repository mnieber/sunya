from django.contrib.auth import get_user_model

from common.form_serializer import FormSerializer
from common.serializers import BaseModelSerializer, ReadSerializerMixin
from users.actions.create_user import CreateUserForm
from users.actions.sign_in_user import SignInUserForm

User = get_user_model()


class CreateUserFormSerializer(FormSerializer):
    class Meta:
        form_class = CreateUserForm


class SignInUserFormSerializer(FormSerializer):
    class Meta:
        form_class = SignInUserForm


class UserSerializer(ReadSerializerMixin, BaseModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "is_active"]
