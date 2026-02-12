from django.contrib.auth import get_user_model

from darshana_be.common.form_serializer import FormSerializer
from darshana_be.common.serializers import BaseModelSerializer, ReadSerializerMixin
from darshana_be.users.actions.create_user import CreateUserForm
from darshana_be.users.actions.sign_in_user import SignInUserForm
from rest_framework.serializers import Serializer, UUIDField


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


class TokenValidateSerializer(Serializer):
    token = UUIDField()
