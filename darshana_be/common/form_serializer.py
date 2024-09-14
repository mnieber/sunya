from argparse import Namespace
from typing import Union, get_args, get_origin, Any
from uuid import UUID

import rest_framework_gis.fields
from django.contrib.gis.geos import Polygon
from rest_framework import serializers


class FormSerializer(serializers.Serializer):
    def __init_subclass__(cls, **kwargs):
        form_class = _get_form_class(cls)
        for field_name, annotated_field_type in form_class.__annotations__.items():
            if field_name in cls._declared_fields:
                continue

            optional, field_type = _is_optional_type(annotated_field_type)
            if not field_type:
                raise Exception(
                    f"Unsupported optional type {field_type}. "
                    + f"Please check the '{field_name}' field."
                )

            is_list = _is_list_type(field_type)
            is_dict = _is_dict_type(field_type)

            field_kwargs = {}
            if not (is_list or is_dict) and optional:
                field_kwargs["required"] = False
                if not field_type == bool:
                    field_kwargs["allow_blank"] = True
                    field_kwargs["allow_null"] = True

            if is_list:
                item_type = get_args(field_type)[0]
                field = serializers.ListField(child=_get_serializer_field(item_type))
            elif is_dict:
                key_type, value_type = get_args(field_type)
                field = _create_dict_field(key_type, value_type, **field_kwargs)
            else:
                field = _get_serializer_field(field_type, **field_kwargs)

            if optional and not field_kwargs.get("required") == False:
                field.required = False

            if not field_name.startswith("__"):
                cls._declared_fields[field_name] = field

        super().__init_subclass__(**kwargs)

    def validate(self, data):
        return _get_form_class(self)(**data)


def _is_list_type(field_type):
    return get_origin(field_type) == list


def _is_dict_type(field_type):
    return get_origin(field_type) == dict


def _is_optional_type(field_type):
    if get_origin(field_type) == Union:
        args = get_args(field_type)
        none_arg = [arg for arg in args if arg == type(None)]
        some_args = [arg for arg in args if arg != type(None)]
        some_arg = next(iter(some_args), None)
        return bool(none_arg), some_arg
    return False, field_type


def _get_form_class(cls):
    if hasattr(cls, "Meta") and getattr(cls.Meta, "form_class", None):
        return cls.Meta.form_class
    return Namespace


def _get_serializer_field(field_type, **kwargs):
    if field_type == UUID:
        return serializers.UUIDField(**kwargs)
    elif field_type == Polygon:
        return rest_framework_gis.fields.GeometryField(**kwargs)
    elif field_type == str:
        return serializers.CharField(**kwargs)
    elif field_type == int:
        return serializers.IntegerField(**kwargs)
    elif field_type == float:
        return serializers.FloatField(**kwargs)
    elif field_type == bool:
        return serializers.BooleanField(**kwargs)
    elif field_type == Any:
        return serializers.JSONField(**kwargs)
    elif hasattr(field_type, "choices"):
        return serializers.ChoiceField(choices=field_type.choices, **kwargs)
    else:
        raise Exception(f"Unsupported field type: {field_type}")


def _create_dict_field(key_type, value_type, **kwargs):
    child = _get_serializer_field(value_type)

    if key_type == str:
        return serializers.DictField(child=child, **kwargs)
    else:
        return CustomKeyDictField(
            child=child, key_type=_get_serializer_field(key_type), **kwargs
        )


class CustomKeyDictField(serializers.DictField):
    def __init__(self, key_type, *args, **kwargs):
        self.key_type = key_type
        super().__init__(*args, **kwargs)

    def to_internal_value(self, data):
        ret = {}
        for key, value in data.items():
            validated_key = self.key_type.to_internal_value(key)
            validated_value = self.child.to_internal_value(value)
            ret[validated_key] = validated_value
        return ret

    def to_representation(self, value):
        return {
            self.key_type.to_representation(key): self.child.to_representation(value)
            for key, value in value.items()
        }
