from rest_framework import serializers
from rest_framework.serializers import BooleanField, CharField, Serializer, UUIDField

from users.models import TokenScope, UserEmailToken
from users.serializers import LoginResponseSerializer


class TokenLoginSerializer(Serializer):
    token = CharField()

    def validate_token(self, value):
        return UserEmailToken.use_token(
            value, scopes=[TokenScope.PASSWORD_RESET, TokenScope.IMPERSONATE]
        )


class TokenValidateSerializer(Serializer):
    token = UUIDField()


class TokenValidateResponseSerializer(Serializer):
    valid = BooleanField()


class OTPLoginResponseSerializer(LoginResponseSerializer):
    impersonated_by = CharField(allow_null=True, required=False)


class SignOutSerializer(Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()


class RefreshTokenSerializer(Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()
