from rest_framework import serializers
from steps.models import Step
from common.serializers import BaseModelSerializer, ReadSerializerMixin
from dataclassy import asdict


class FactBitSerializer(serializers.Serializer):
    type_name = serializers.ChoiceField(choices=["string", "role", "actor"])
    value = serializers.CharField()
    child_steps = serializers.SerializerMethodField()

    def to_representation(self, instance):
        return asdict(instance)


class StepSerializer(ReadSerializerMixin, BaseModelSerializer):
    fact = FactBitSerializer(many=True)
    child_steps = serializers.SerializerMethodField()

    class Meta:
        model = Step
        fields = [
            "id",
            "fact",
            "parent_step",
            "field_delta_set_by_actor_key",
            "child_steps",
        ]

    def get_child_steps(self, obj):
        if not obj.child_steps.all():
            return []

        return StepSerializer(obj.child_steps.all(), many=True).data
